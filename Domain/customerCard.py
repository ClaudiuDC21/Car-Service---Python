import datetime
from dataclasses import dataclass

from Domain.entity import Entity


@dataclass
class CustomerCard(Entity):
    nume: str
    prenume: str
    CNP: int  # must be unique
    data_nasterii: datetime.date
    data_inregistrarii: datetime.date
