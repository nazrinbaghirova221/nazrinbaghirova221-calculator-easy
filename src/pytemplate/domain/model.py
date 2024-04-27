from dataclasses import dataclass
from typing import Union


@dataclass(frozen=True)
class Operand:
  first_operand: Union[int, float]
  second_operand: Union[int, float]