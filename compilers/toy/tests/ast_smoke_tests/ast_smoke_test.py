"""Print AST of all sources in a test stage.

Valid sources should produce an AST, invalid sources should cause a compiler
diagnostic.
"""
import pathlib
import subprocess

from compilers.toy.tests import smoke_test_flags
from labm8.py import app
from labm8.py import bazelutil
from labm8.py import fs
from labm8.py import test

FLAGS = smoke_test_flags.FLAGS

_TEST_DATA_ROOT = bazelutil.DataPath("phd/compilers/toy/test_data")
# Frustratingly, the go binary does not have the name of the binary.
_print_ast_files = list(
  bazelutil.DataPath("phd/compilers/toy/util/print_ast").iterdir()
)
assert len(_print_ast_files) == 1
_PRINT_AST = _print_ast_files[0] / "print_ast"
assert fs.isexe(_PRINT_AST)

MODULE_UNDER_TEST = None  # Disable coverage.


def PrintAST(path: pathlib.Path) -> bool:
  """Run lexer on path. Raises an exception is the lexer fails."""
  app.Log(1, "Printing AST of %s:\n%s", path, fs.read(path))
  process = subprocess.Popen(
    [str(_PRINT_AST), "-logtostderr", "-v=2", str(path)]
  )
  process.communicate()
  testpass = process.returncode == 0
  test.Log(
    "Returncode: %s (%s)", process.returncode, "PASS" if testpass else "FAIL"
  )
  return testpass


def TestStage(stage: int):
  """Lex all files for the given stage and check that they all work."""
  assert 1 <= stage <= 10

  valid_files = fs.lsfiles(
    _TEST_DATA_ROOT / f"stage_{stage}" / "valid", abspaths=True
  )
  invalid_files = fs.lsfiles(
    _TEST_DATA_ROOT / f"stage_{stage}" / "invalid", abspaths=True
  )

  for test_file in valid_files:
    if pathlib.Path(test_file).name.startswith("skip_on_failure"):
      continue
    testpass = PrintAST(test_file)
    if FLAGS.xfail:
      assert not testpass
    else:
      assert testpass

  for test_file in invalid_files:
    # --xfail does not affect the expected outcome of failing tests.
    assert not PrintAST(test_file)


def test_stage():
  """Run stage tests."""
  TestStage(FLAGS.stage)


if __name__ == "__main__":
  test.Main()
