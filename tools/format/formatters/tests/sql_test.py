# Copyright 2020 Chris Cummins <chrisc.101@gmail.com>.
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
"""Unit tests for //tools/format/formatters:sql."""
from labm8.py import test
from tools.format.formatters import sql

FLAGS = test.FLAGS


def test_format_single_query():
  text = sql.FormatSql.Format(
    """
select * from users;"""
  )
  print(text)
  assert (
    text
    == """
SELECT *
FROM users;
"""
  )


def test_format_empty_file():
  assert sql.FormatSql.Format("") == "\n"


def test_format_hello_world():
  assert sql.FormatSql.Format("Hello world") == "Hello world\n"


def test_format_sql_query():
  assert (
    sql.FormatSql.Format("select count(*),foo.bar from foo;")
    == """\
SELECT count(*),
       foo.bar
FROM foo;
"""
  )


if __name__ == "__main__":
  test.Main()
