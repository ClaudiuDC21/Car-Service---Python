from dataclasses import dataclass

from Domain.entity import Entity


@dataclass
class Car(Entity):
    model: str
    an_achizitie: int  # must be positive
    nr_km: float  # must be pozitive
    in_garantie: str  # must be yes/no
