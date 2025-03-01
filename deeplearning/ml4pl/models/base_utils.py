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
from typing import List
from typing import Union

import numpy as np

from labm8.py import app


FLAGS = app.FLAGS

app.DEFINE_float("initial_learning_rate", 0.001, "The initial learning rate.")
app.DEFINE_boolean(
  "use_lr_schedule",
  False,
  "Whether to use a warmup-train-finetune learning rate schedule.",
)


def pos_emb(
  positions: Union[int, List[int], np.array], demb: int = 200, dpad: int = 2
):
  """Transformer-like sinusoidal positional embeddings.
        Args:
        position: int or array of ints   positions to embed,
        demb: int    size of embedding vector
    """
  inv_freq = 1 / (10000 ** (np.arange(0.0, demb, 2.0) / demb))

  sinusoid_inp = np.outer(positions, inv_freq)
  pos_emb = np.hstack((np.sin(sinusoid_inp), np.cos(sinusoid_inp)))

  if dpad > 0:
    in_length = 1 if type(positions) == int else len(positions)
    pad = np.zeros([in_length, dpad])
    pos_emb = np.hstack([pos_emb, pad])
    assert np.all(
      pos_emb[:, -1] == np.zeros(in_length)
    ), f"test failed. pos_emb: \n{pos_emb}"
  return pos_emb


def WarmUpAndFinetuneLearningRateSchedule(
  curr_epoch: int, total_epochs: int
) -> float:
  """splits epochs into warmup, training, and finetuning:
      10% but minimum 1 and maximum 10 epochs of quadratic warmup from 0 to learning_rate,
      60% training with learning_rate
      15% learning_rate * 0.1
      15% learning_rate * 0.01
  """
  assert total_epochs is not None
  assert curr_epoch is not None

  if not FLAGS.use_lr_schedule:
    return 1.0

  warmup_epochs = float(np.clip(total_epochs * 0.1, 1, 10))
  if curr_epoch <= warmup_epochs:
    factor = min(1.0, curr_epoch ** 2 / warmup_epochs ** 2 + 0.01)
  elif curr_epoch <= 0.7 * total_epochs:
    factor = 1.0
  elif curr_epoch <= 0.85 * total_epochs:
    factor = 0.1
  else:
    factor = 0.01
  return factor


SMALL_NUMBER = 1e-7

# alternatively could use something like this:

# def GetLearningRate(epoch_num: int) -> float:
#  """Compute the learning rate.
#
#  Args:
#    epoch_num: The (zero-based) epoch number.
#
#  Returns:
#     A learning rate, in range (0,inf).
#  """
#  return FLAGS.initial_learning_rate / (
#      1 + FLAGS.initial_learning_rate_exponential_decay * epoch_num)
