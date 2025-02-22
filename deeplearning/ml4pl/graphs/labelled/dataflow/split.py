# Copyright 2019-2020 the ProGraML authors.
#
# Contact Chris Cummins <chrisc.101@gmail.com>.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Split a labelled graph database into {train,val,test} sets."""
import sqlalchemy as sql

from deeplearning.ml4pl.graphs.labelled import graph_tuple_database
from deeplearning.ml4pl.ir import ir_database
from deeplearning.ml4pl.ir import split as ir_split
from labm8.py import app
from labm8.py import humanize
from labm8.py import labtypes
from labm8.py import prof


FLAGS = app.FLAGS

app.DEFINE_database(
  "copy_splits_to",
  graph_tuple_database.Database,
  None,
  "If set, this is a database to copy the split column to.",
)


class TrainValTestSplitter(ir_split.TrainValTestSplitter):
  """{train,val,test} split across intermediate representations."""

  def ApplySplit(
    self, graph_db: graph_tuple_database.Database, ir_db: ir_database.Database
  ) -> None:
    """Set the split values on the given database."""
    for split, ir_ids in enumerate(self.Split(ir_db)):
      with prof.Profile(
        f"Set {split} split on {humanize.Plural(len(ir_ids), 'IR')}"
      ):
        for chunk in labtypes.Chunkify(ir_ids, 10000):
          update = (
            sql.update(graph_tuple_database.GraphTuple)
            .where(graph_tuple_database.GraphTuple.ir_id.in_(chunk))
            .values(split=split)
          )
          graph_db.engine.execute(update)


def CopySplits(
  input_db: graph_tuple_database.Database,
  output_db: graph_tuple_database.Database,
):
  """Propagate the `split` column from one database to another."""
  # Unset splits on output database.
  with prof.Profile(f"Unset splits on {output_db.graph_count} graphs"):
    update = sql.update(graph_tuple_database.GraphTuple).values(split=None)
    output_db.engine.execute(update)

  # Copy each split one at a time.
  for split in input_db.splits:
    with prof.Profile(f"Copied split {split}"):
      with input_db.Session() as in_session:
        ids_to_set = [
          row.id
          for row in in_session.query(
            graph_tuple_database.GraphTuple.id
          ).filter(graph_tuple_database.GraphTuple.split == split)
        ]

      update = (
        sql.update(graph_tuple_database.GraphTuple)
        .where(graph_tuple_database.GraphTuple.id.in_(ids_to_set))
        .values(split=split)
      )
      output_db.engine.execute(update)


def main():
  """Main entry point."""
  if FLAGS.copy_splits_to:
    CopySplits(FLAGS.graph_db(), FLAGS.copy_splits_to())
  else:
    TrainValTestSplitter(FLAGS.train_val_test_ratio).ApplySplit(
      FLAGS.graph_db(), FLAGS.ir_db()
    )


if __name__ == "__main__":
  app.Run(main)
