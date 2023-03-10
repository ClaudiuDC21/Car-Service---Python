from dataclasses import dataclass
from typing import List


@dataclass
class CustomerCardError(Exception):
    error_message: List[str]

    def __str__(self):
        return f"CustomerCardError: {self.error_message}"
