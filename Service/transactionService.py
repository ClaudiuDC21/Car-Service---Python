from datetime import datetime
from typing import List

from Domain.transaction import Transaction
from Domain.transactionValidator import TransactionValidator
from Repository.jsonRepository import JsonRepository



class TransactionService:
    def __init__(self,
                 transaction_repository: JsonRepository,
                 transaction_validator: TransactionValidator,
                 car_repository: JsonRepository,
                 customer_card_repository: JsonRepository):
        self.transaction_repository = transaction_repository
        self.transaction_validator = transaction_validator
        self.car_repository = car_repository
        self.customer_card_repository = customer_card_repository


    def add_transaction(self, id_entity: str, id_car: str,
                        id_customer_card: str, suma_piese: float,
                        suma_manopera: float, dateandtime: datetime,
                        total: float, sale: float):
        """
        Adauga o tranzactie in baza de date.
        :param id_entity: Id-ul transactiei.
        :param id_car: Id-ul masinii.
        :param id_customer_card: Id-ul cardului de client, poate fi si null.
        :param suma_piese: Suma pieselor.
        :param suma_manopera: Suma manoperei.
        :param dateandtime: Data si ora tranzactiei.
        :param total: Suma platita.
        :param sale: Reducerile obtinute.
        :return: O lista cu tranzactia adaugata.
        """

        garantie = self.car_repository.read(id_car).in_garantie
        if garantie == 'da':
            noua_suma_piese = 0
            reducere = suma_piese
        else:
            noua_suma_piese = suma_piese
            reducere = 0

        id_card_client = self.customer_card_repository.read(
            id_customer_card).id_entity
        if id_card_client != 'null':
            nou_suma_manopera = suma_manopera - (1 / 10) * suma_manopera
            reducere_suma_manopera = 1 / 10 * suma_manopera
        else:
            nou_suma_manopera = suma_manopera
            reducere_suma_manopera = 0
        total = nou_suma_manopera + noua_suma_piese
        sale = reducere_suma_manopera + reducere
        transaction = Transaction(id_entity, id_car, id_customer_card,
                                  noua_suma_piese, nou_suma_manopera,
                                  dateandtime, total, sale)
        if self.car_repository.read(id_car) is None:
            raise KeyError(f'Nu exista o masina cu id-ul {id_car}. ')
        if self.customer_card_repository.read(id_customer_card) is None:
            raise KeyError(f'Nu exista un card cu id-ul {id_customer_card}')
        self.transaction_validator.validate(transaction)
        self.transaction_repository.create(transaction)


    def update_transaction(self, id_entity: str, id_car: str,
                           id_customer_card: str, suma_piese: float,
                           suma_manopera: float,
                           dateandtime: datetime, total: float,
                           sale: float):
        """
        Modifica o tranzactie in baza de date.
        :param id_entity: Id-ul transactiei.
        :param id_car: Id-ul masinii.
        :param id_customer_card: Id-ul cardului de client, poate fi si null.
        :param suma_piese: Suma pieselor.
        :param suma_manopera: Suma manoperei.
        :param dateandtime: Data si ora tranzactiei.
        :param total: Suma platita.
        :param sale: Reducerile obtinute.
        :return: O lista cu tranzactia modificata.
        """
        garantie = self.car_repository.read(id_car).in_garantie
        if garantie == 'da':
            noua_suma_piese = 0
            reducere = suma_piese
        else:
            noua_suma_piese = suma_piese
            reducere = 0

        id_card_client = self.customer_card_repository.read(
            id_customer_card).id_entity
        if id_card_client != 'null':
            nou_suma_manopera = suma_manopera - (1 / 10) * suma_manopera
            reducere_suma_manopera = 1 / 10 * suma_manopera
        else:
            nou_suma_manopera = suma_manopera
            reducere_suma_manopera = 0
        total = nou_suma_manopera + noua_suma_piese
        sale = reducere_suma_manopera + reducere
        transaction = Transaction(id_entity, id_car, id_customer_card,
                                  noua_suma_piese, nou_suma_manopera,
                                  dateandtime, total, sale)
        if self.car_repository.read(id_car) is None:
            raise KeyError(f'Nu exista o masina cu id-ul {id_car}. ')
        if self.customer_card_repository.read(id_customer_card) is None:
            raise KeyError(f'Nu exista un card cu id-ul {id_customer_card}. ')
        self.transaction_validator.validate(transaction)
        self.transaction_repository.update(transaction)

    def delete_transaction(self, id_entity: str):
        """
        Sterge o tranzactie.
        :param id_entity: Id-ul tranzactiei..
        :return: Lista cu tranzactia stearsa.
        """
        self.transaction_repository.delete(id_entity)

    def get_all(self) -> List[Transaction]:
        return self.transaction_repository.read()

    def show_transactions_in_interval(self, begin_interval: float,
                                      end_interval: float):
        """
        Afișarea tuturor tranzacțiilor cu suma cuprinsă într-un interval dat.
        :param begin_interval: Inceputul intervalului.
        :param end_interval: Sfarsitul Intervalului.
        :return: Tranzactiile cu suma cuprinsa in intervalul dat.
        """
        interval = [tranzactie for tranzactie in
                    self.transaction_repository.read() if begin_interval <=
                    tranzactie.suma_manopera + tranzactie.suma_piese <=
                    end_interval]
        return interval

    def delete_all_tranzactions_on_some_days(self, begin_date: datetime.date,
                                             end_date: datetime.date):
        """
        Sterge toate tranzactiile intr-un interval de zile dat.
        :param begin_date: Inceputul intervalului.
        :param end_date:  Sfarsitul intervalului.
        """
        [self.transaction_repository.delete(transaction.id_entity)
         for transaction in self.transaction_repository.read()
         if begin_date < transaction.dateandtime < end_date]

    def cascade_delete(self, id_entity: str) -> None:
        """
        Sterge un obiect de tip CustomerCard.
        :param id_entity: Id-ul entitatii.
        """
        cascade = []
        transactions = self.transaction_repository.read()
        for transaction in transactions:
            if transaction.id_customer_card == id_entity:
                cascade.append(transaction)
                self.transaction_repository.delete(transaction.id_entity)

        customer_card = self.customer_card_repository.read(id_entity)
        cascade.append(customer_card)

        self.customer_card_repository.delete()
