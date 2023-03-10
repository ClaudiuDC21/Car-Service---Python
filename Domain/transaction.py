import datetime
from dataclasses import dataclass

from Domain.entity import Entity


@dataclass
class Transaction(Entity):
    id_car: str
    id_customer_card: str  # poate fi null
    suma_piese: float
    suma_manopera: float
    dateandtime: datetime.datetime
    total: float
    sale: float
