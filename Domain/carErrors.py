from dataclasses import dataclass
from typing import List


@dataclass
class CarError(Exception):
    error_message: List[str]

    def __str__(self):
        return f"CarError: {self.error_message}"
