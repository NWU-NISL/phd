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
"""Run the device mapping models.

Usage:

    $ bazel run //deeplearning/ml4pl/experiments/devmap:run_models -- \
        --db_stem='sqlite:////tmp/programl/db/'
        --dataset=amd,nvidia \
        --model=zero_r,lstm_opencl,lstm_ir,lstm_inst2vec,ggnn \
        --tag_suffix=v1
"""
import time

from deeplearning.ml4pl.graphs.labelled import graph_tuple_database
from deeplearning.ml4pl.ir import ir_database
from deeplearning.ml4pl.models import log_database
from deeplearning.ml4pl.models import run
from deeplearning.ml4pl.models.ggnn import ggnn
from deeplearning.ml4pl.models.lstm import lstm
from deeplearning.ml4pl.models.zero_r import zero_r
from labm8.py import app
from labm8.py.internal import flags_parsers

FLAGS = app.FLAGS

app.DEFINE_list(
  "dataset",
  ["amd", "nvidia"],
  "The name of the dataset to evaluate. One of {amd,nvidia}.",
)
app.DEFINE_list(
  "model",
  ["zero_r", "lstm_opencl", "lstm_ir", "lstm_inst2vec", "ggnn"],
  "The names of the models to evaluate.",
)
app.DEFINE_string(
  "tag_suffix",
  f"v{time.strftime('%y-%m-%dT%H:%M:%S')}",
  "The tag suffix to use for runs.",
)
app.DEFINE_string(
  "db_stem",
  "file:///var/phd/db/cc1.mysql?programl",
  "The stem for database names.",
)


def Main():
  """Main entry point."""
  db_stem = FLAGS.db_stem
  models = FLAGS.model
  tag_suffix = FLAGS.tag_suffix
  datasets = FLAGS.dataset

  # Set model and dataset-invariant flags.
  FLAGS.log_db = flags_parsers.DatabaseFlag(
    log_database.Database, f"{db_stem}_devmap_logs", must_exist=True
  )
  FLAGS.ir_db = flags_parsers.DatabaseFlag(
    ir_database.Database, f"{db_stem}_ir", must_exist=True
  )
  FLAGS.k_fold = True
  FLAGS.test_on = "improvement_and_last"

  for dataset in datasets:
    # Set model-invariant flags.
    FLAGS.graph_db = flags_parsers.DatabaseFlag(
      graph_tuple_database.Database,
      f"{db_stem}_devmap_{dataset}",
      must_exist=True,
    )

    for model in models:
      FLAGS.tag = f"devmap_{dataset}_{model}_{tag_suffix}"

      if model == "zero_r":
        FLAGS.epoch_count = 1
        run.Run(zero_r.ZeroR)
      elif model == "lstm_opencl":
        FLAGS.epoch_count = 50
        FLAGS.ir2seq = flags_parsers.EnumFlag(
          lstm.Ir2SeqType, lstm.Ir2SeqType.OPENCL
        )
        FLAGS.padded_sequence_length = 1024
        FLAGS.batch_size = 64
        run.Run(lstm.GraphLstm)
      elif model == "lstm_ir":
        FLAGS.epoch_count = 50
        FLAGS.ir2seq = flags_parsers.EnumFlag(
          lstm.Ir2SeqType, lstm.Ir2SeqType.LLVM
        )
        FLAGS.padded_sequence_length = 15000
        FLAGS.batch_size = 64
        run.Run(lstm.GraphLstm)
      elif model == "lstm_inst2vec":
        FLAGS.epoch_count = 50
        FLAGS.ir2seq = flags_parsers.EnumFlag(
          lstm.Ir2SeqType, lstm.Ir2SeqType.INST2VEC
        )
        FLAGS.padded_sequence_length = 15000
        FLAGS.batch_size = 64
        run.Run(lstm.GraphLstm)
      elif model == "ggnn":
        # Reduced batch size because OOM errors with larger batches on my
        # NVIDIA GTX 1080 GPU.
        FLAGS.graph_batch_size = 32
        FLAGS.epoch_count = 100
        run.Run(ggnn.Ggnn)
      else:
        raise app.UsageError(f"Unknown model: {model}")


if __name__ == "__main__":
  app.Run(Main)
