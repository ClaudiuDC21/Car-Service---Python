import datetime
from typing import List


from Domain.customerCard import CustomerCard
from Domain.customerCardValidator import CustomerCardValidator
from Repository.jsonRepository import JsonRepository



class CustomerCardService:
    def __init__(self, customer_card_repository: JsonRepository,
                 customer_card_validator: CustomerCardValidator,
                 transaction_repository: JsonRepository):
        self.customer_card_repository = customer_card_repository
        self.customer_card_validator = customer_card_validator
        self.transaction_repository = transaction_repository

    def add_customer_card(self, id_entity: str, nume: str, prenume: str,
                          CNP: int, data_nasterii: datetime.date,
                          data_inregistrarii: datetime.date):
        """
        Adauga un card de client in baza de date.
        :param id_entity: Id-ul cardului de clint.
        :param nume: Numele clientului.
        :param prenume: Prenumele clientului.
        :param CNP: CNP-ul clientului.
        :param data_nasterii: Data de nastere a clientului.
        :param data_inregistrarii: Data de inregistrare a clientului.
        :return: Lista modificata cu cardul de client adaugat.
        """
        for card in self.customer_card_repository.read():
            if card.CNP == CNP:
                raise KeyError(
                    'Clientul cu acest CNP are deja un card de client. ')

        customer_card = CustomerCard(id_entity, nume, prenume, CNP,
                                     data_nasterii, data_inregistrarii)
        self.customer_card_validator.validate(customer_card)
        self.customer_card_repository.create(customer_card)


    def update_customer_card(self, id_entity: str, nume: str,
                             prenume: str, CNP: int,
                             data_nasterii: datetime.date,
                             data_inregistrarii: datetime.date):
        """
        Modifica un card de client in baza de date.
        :param id_entity: Id-ul cardului de clint.
        :param nume: Numele clientului.
        :param prenume: Prenumele clientului.
        :param CNP: CNP-ul clientului.
        :param data_nasterii: Data de nastere a clientului.
        :param data_inregistrarii: Data de inregistrare a clientului.
        :return: Lista modificata cu cardul de client modificat.
        """

        customer_card = CustomerCard(id_entity, nume, prenume, CNP,
                                     data_nasterii, data_inregistrarii)
        self.customer_card_validator.validate(customer_card)
        self.customer_card_repository.update(customer_card)

    def delete_customer_card(self, id_entity: str):
        """
        Sterge o masina.
        :param id_entity: Id-ul masinii.
        :return: Lista cu masina stearsa.
        """
        self.customer_card_repository.delete(id_entity)

    def get_all(self) -> List[CustomerCard]:
        return self.customer_card_repository.read()

    def full_text_search_customers(self, search: str) -> List[CustomerCard]:
        """
        Cauta sirul de caractere dat in toate entitatile din CustomerCard,
        oricare ar fi acestea.
        :param search: Sirul de caractere cautat.
        :return: Lista cu entitatile ce contin string-ul dat.
        """
        result = []
        customer_card_repository = self.customer_card_repository.read()
        for customer_card in customer_card_repository:
            birthday_str = customer_card.data_nasterii.strftime("%d %m %y")
            inregistration_str = customer_card.data_inregistrarii.strftime(
                "%d %m %y")
            if search in customer_card.nume or \
                    search in customer_card.prenume or \
                    search in str(customer_card.CNP) or \
                    search in birthday_str or \
                    search in inregistration_str:
                result.append(customer_card)
        return result

    def show_client_card_descending_after_sale(self):
        """
        Afișarea cardurilor client ordonate descrescător după valoarea
         reducerilor obținute.
        :return: Lista de carduri ordonate descrecator dupa reduceri.
        """
        result = []
        for cards in self.customer_card_repository.read():
            reducere_tranzactie = [reducere.sale for reducere in
                                   self.transaction_repository.read()
                                   if reducere.id_customer_card ==
                                   cards.id_entity]
            result.append((cards, reducere_tranzactie))
        return sorted(result, key=lambda x: x[1], reverse=True)
