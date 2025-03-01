# Copyright 2017-2020 Chris Cummins <chrisc.101@gmail.com>.
#
# This file is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""Unit tests for //research/cummins_2017_cgo:opencl_kernel_driver."""
from gpu.cldrive.legacy import env as cldrive_env
from labm8.py import app
from labm8.py import test
from research.cummins_2017_cgo import opencl_kernel_driver

FLAGS = app.FLAGS


@test.Fixture(scope="function")
def opencl_env() -> cldrive_env.OpenCLEnvironment:
  """A test fixture which yields an OpenCL environment for testing."""
  return cldrive_env.OclgrindOpenCLEnvironment()


def test_Drive_invalid_opencl_kernel(opencl_env: cldrive_env.OpenCLEnvironment):
  """Test that the correct number of logs are returned."""
  with test.Raises(opencl_kernel_driver.DriverConstructionFailed):
    opencl_kernel_driver.Drive("Syntax error!", 16, 16, opencl_env, 5)


@test.XFail(reason="FIXME(github.com/ChrisCummins/phd/issues/69)")
def test_Drive_no_output(opencl_env: cldrive_env.OpenCLEnvironment):
  """Test that the correct number of logs are returned."""
  with test.Raises(opencl_kernel_driver.KernelProducesNoOutput):
    opencl_kernel_driver.Drive(
      """
kernel void A(global int* a, global int* b) {
}
""",
      16,
      16,
      opencl_env,
      5,
    )


@test.XFail(reason="FIXME(github.com/ChrisCummins/phd/issues/69)")
def test_Drive_maybe_non_deterministic(
  opencl_env: cldrive_env.OpenCLEnvironment,
):
  """Test that the correct number of logs are returned.

  FLAKY TEST: There is no guarantee that the kernel will produce
  non-deterministic results. I've "encouraged" non-determinism by accessing
  out of bounds and dividing by zero.
  """
  with test.Raises(opencl_kernel_driver.KernelIsNondeterministic):
    opencl_kernel_driver.Drive(
      """
kernel void A(global float* a, global float* b) {
  a[get_global_id(0)] = b[-get_global_id(0)] / (get_global_id(0) == 0 ? 0 : 1);
}
""",
      16,
      16,
      opencl_env,
      5,
    )


@test.XFail(reason="FIXME(github.com/ChrisCummins/phd/issues/69)")
def test_Drive_log_count(opencl_env: cldrive_env.OpenCLEnvironment):
  """Test that the correct number of logs are returned."""
  logs = opencl_kernel_driver.Drive(
    """
kernel void A(global int* a, global int* b) {
  a[get_global_id(0)] += b[get_global_id(0)];
}
""",
    16,
    16,
    opencl_env,
    5,
  )
  assert len(logs) == 5


if __name__ == "__main__":
  test.Main()
