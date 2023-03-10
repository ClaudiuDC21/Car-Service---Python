import datetime

from Domain.car import Car
from Domain.customerCard import CustomerCard
from Domain.transaction import Transaction


def test_car():
    masina = Car('1', 'Logan', 2005, 205467.12, 'nu')
    assert masina.id_entity == '1'
    assert masina.model == 'Logan'
    assert masina.an_achizitie == 2005
    assert masina.nr_km == 205467.12
    assert masina.in_garantie == 'nu'
    masina.id_entity = '2'
    masina.model = 'BMW'
    masina.an_achizitie = 2017
    masina.nr_km = 124234.23
    masina.in_garantie = 'da'
    assert masina.id_entity == '2'
    assert masina.model == 'BMW'
    assert masina.an_achizitie == 2017
    assert masina.nr_km == 124234.23
    assert masina.in_garantie == 'da'


def test_customer_card():
    card_client = CustomerCard('300', 'Popescu', 'Dan', 5011211330234,
                               datetime.date(2021, 3, 4),
                               datetime.date(2021, 4, 13))
    assert card_client.id_entity == '300'
    assert card_client.nume == 'Popescu'
    assert card_client.prenume == 'Dan'
    assert card_client.CNP == 5011211330234
    assert card_client.data_nasterii == datetime.date(2021, 3, 4)
    assert card_client.data_inregistrarii == datetime.date(2021, 4, 13)
    card_client.id_entity = '301'
    card_client.nume = 'Danciulescu'
    card_client.prenume = 'Iordache'
    card_client.CNP = 1950624339197
    card_client.data_nasterii = datetime.date(1995, 6, 24)
    card_client.data_inregistrarii = datetime.date(2020, 5, 17)
    assert card_client.id_entity == '301'
    assert card_client.nume == 'Danciulescu'
    assert card_client.prenume == 'Iordache'
    assert card_client.CNP == 1950624339197
    assert card_client.data_nasterii == datetime.date(1995, 6, 24)
    assert card_client.data_inregistrarii == datetime.date(2020, 5, 17)


def test_transaction():
    tranzactie = Transaction('100', '1', 'null', 250, 100,
                             datetime.datetime(2021, 11, 15, 12, 24, 48), 0, 0)
    assert tranzactie.id_entity == '100'
    assert tranzactie.id_car == '1'
    assert tranzactie.id_customer_card == 'null'
    assert tranzactie.suma_piese == 250
    assert tranzactie.suma_manopera == 100
    assert tranzactie.dateandtime == datetime.datetime(2021, 11, 15, 12, 24,
                                                       48)
    tranzactie.id_entity = '101'
    tranzactie.id_car = '2'
    tranzactie.id_customer_card = '1000'
    tranzactie.suma_piese = 400
    tranzactie.suma_manopera = 153
    tranzactie.dateandtime = datetime.datetime(2016, 4, 28, 9, 32, 59)
    assert tranzactie.id_entity == '101'
    assert tranzactie.id_car == '2'
    assert tranzactie.id_customer_card == '1000'
    assert tranzactie.suma_piese == 400
    assert tranzactie.suma_manopera == 153
    assert tranzactie.dateandtime == datetime.datetime(2016, 4, 28, 9, 32, 59)


def test_domain():
    test_car()
    test_transaction()
    test_customer_card()
