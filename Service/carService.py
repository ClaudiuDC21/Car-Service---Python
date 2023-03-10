import random
import string
from typing import List

from Domain.car import Car
from Domain.carValidator import CarValidator
from Repository.jsonRepository import JsonRepository


class CarService:
    def __init__(self, car_repository: JsonRepository,
                 car_validator: CarValidator,
                 transaction_repository: JsonRepository):
        self.car_repository = car_repository
        self.car_validator = car_validator
        self.transaction_repository = transaction_repository

    def add_car(self, id_entity: str, model: str, an_achizitie: int,
                nr_km: float, in_garantie: str):
        """
        Adauga o masina.
        :param id_entity: Id-ul masinii.
        :param model: Modelul masinii.
        :param an_achizitie: Anul achizitiei.
        :param nr_km: Numarul de kolimetrii
        :param in_garantie: Confirma daca este in garantie: da / nu.
        :return: Masina adaugata in lista.
        """
        car = Car(id_entity, model, an_achizitie, nr_km, in_garantie)
        self.car_validator.validate(car)
        self.car_repository.create(car)

    def update_car(self, id_entity: str, model: str, an_achizitie: int,
                   nr_km: float, in_garantie: str):
        """
        Modifica o masina.
        :param id_entity: Id-ul masinii.
        :param model: Modelul masinii.
        :param an_achizitie: Anul achizitiei.
        :param nr_km: Numarul de kolimetrii
        :param in_garantie: Confirma daca este in garantie: da / nu.
        :return: Masina modificata in lista.
        """
        car = Car(id_entity, model, an_achizitie, nr_km, in_garantie)
        self.car_validator.validate(car)
        self.car_repository.update(car)

    def delete_car(self, id_entity: str):
        """
        Sterge o masina.
        :param id_entity: Id-ul masinii.
        :return: Lista cu masina stearsa.
        """
        self.car_repository.delete(id_entity)

    def get_all(self) -> List[Car]:
        return self.car_repository.read()

    def get_n_random_values(self, n: int):
        """
        Creeaza n masini random.
        :param n: Numarul de masini random ce trebuie creeate.
        """
        try:
            for i in range(n):
                cars = int(len(self.get_all()))
                id_car = str(cars + 1)
                model = ''.join(random.choices(string.ascii_letters, k=5))
                data = int(random.randint(1950, 2021))
                nr_km = round(random.uniform(0, 300000), 2)
                in_garantie = random.choice(["da", "nu"])
                self.add_car(id_car, model, data, nr_km,
                             in_garantie)

        except ValueError as ve:
            print(f'Eroare: {ve}')
        except KeyError as ke:
            print(f'Eroare: {ke}')
        except Exception as ex:
            print(f'Eroare: {ex}')

    def full_text_search_car(self, search: str) -> List[Car]:
        """
        Cauta sirul de caractere dat in toate entitatile din CAr, oricare
        ar fi acestea.
        :param search: Sirul de caractere cautat.
        :return: Lista cu entitatile ce contin string-ul dat.
        """
        result = []
        car_repository = self.car_repository.read()
        for car in car_repository:
            if search in car.model or \
                    search in str(car.nr_km) or \
                    search in str(car.an_achizitie) or \
                    search in car.in_garantie:
                result.append(car)
        return result

    def show_cars_descending_by_suma_manopera(self):
        """
        Afișarea mașinilor ordonate descrescător după suma
        obținută pe manoperă.
        """

        def inner(cars):
            if not cars:
                return []

            car = cars[0]
            return [car, ]


        cars = self.get_all()
        result = inner(cars)

        result = []
        for cars in self.car_repository.read():
            suma = [manopera.suma_manopera for manopera in
                    self.transaction_repository.read()
                    if manopera.id_car == cars.id_entity]
            result.append((cars, suma))

        return sorted(result, key=lambda x: x[1], reverse=True)

    def update_waranty_on_every_car(self):
        """
        Actualizarea garanției la fiecare mașină: o mașină este în garanție
        dacă și numai dacă are maxim 3 ani de la achiziție și
        maxim 60 000 de km
        """
        [self.update_car(car.id_entity, car.model, car.an_achizitie,
                         car.nr_km, "da") for car in
         self.car_repository.read() if car.nr_km <= 60000 or
         car.an_achizitie >= 2019]
        [self.update_car(car.id_entity, car.model, car.an_achizitie,
                         car.nr_km, "nu") for car in
         self.car_repository.read() if car.nr_km > 60000 or
         car.an_achizitie < 2019]
