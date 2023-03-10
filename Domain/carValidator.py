from Domain.car import Car
from Domain.carErrors import CarError


class CarValidator:
    @staticmethod
    def validate(car: Car):
        errors = []
        if car.an_achizitie < 0:
            errors.append("Anul achizitiei trebuie sa fie un numar pozitiv. ")
        if car.nr_km < 0:
            errors.append(
                "Numarul de kilometrii trebuie sa fie un numar pozitiv. ")
        if car.in_garantie not in ["da", "nu"]:
            errors.append(
                "Campul 'in garantie' trebuie sa fie 'da' sau 'nu'. ")
        if len(errors) > 0:
            raise CarError(errors)
