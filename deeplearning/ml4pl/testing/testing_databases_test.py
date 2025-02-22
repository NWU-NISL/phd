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
"""Unit tests for //deeplearning/ml4pl/test:testing_database."""
import sqlalchemy as sql

from deeplearning.ml4pl.testing import testing_databases
from labm8.py import sqlutil
from labm8.py import test


FLAGS = test.FLAGS


# Define a simple testing database.
Base = sql.ext.declarative.declarative_base()


class Table(Base, sqlutil.TablenameFromClassNameMixin):
  """A simple table for testing."""

  id = sql.Column(sql.Integer, primary_key=True)
  value = sql.Column(sql.String(10))


class Database(sqlutil.Database):
  """A single table database for testing."""

  def __init__(self, url: str, must_exist: bool = False):
    super(Database, self).__init__(url, Base, must_exist=must_exist)


@test.Fixture(
  scope="function",
  params=testing_databases.GetDatabaseUrls(),
  namer=testing_databases.DatabaseUrlNamer("db"),
)
def empty_db(request) -> Database:
  """A test fixture which yields an empty database."""
  yield from testing_databases.YieldDatabase(Database, request.param)


def test_YieldDatabase_fixture(empty_db: Database):
  """Test that database is empty."""
  with empty_db.Session() as session:
    assert session.query(Table).first() is None


@test.Fixture(
  scope="function",
  params=testing_databases.GetDatabaseUrls(),
  namer=testing_databases.DatabaseUrlNamer("db"),
)
def populated_db(request) -> Database:
  """A test fixture which yields an empty database."""
  with testing_databases.DatabaseContext(Database, request.param) as db:
    with db.Session(commit=True) as session:
      session.add(Table(id=1, value="foo"))
    yield db


def test_DatabaseContext_fixture(populated_db: Database):
  """Test that pre-populated database has expected values."""
  with populated_db.Session() as session:
    table = session.query(Table).first()
    assert table.value == "foo"


if __name__ == "__main__":
  test.Main()
