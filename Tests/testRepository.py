import datetime

from Domain.car import Car
from Domain.customerCard import CustomerCard
from Domain.transaction import Transaction
from Repository.jsonRepository import JsonRepository
from Repository.repositoryInMemory import RepositoryInMemory
from utils import clear_file


def test_car_file_repository():
    filename = "test_cars.json"
    clear_file(filename)
    repository = JsonRepository(filename)
    repository.create(Car('1', 'Logan', 2005, 205467.12, 'nu'))
    assert len(repository.read()) == 1
    assert repository.read("1").model == 'Logan'
    assert repository.read('1').an_achizitie == 2005
    assert repository.read('1').nr_km == 205467.12
    repository.update(Car('1', '1310', 2000, 153455.42, 'nu'))
    assert repository.read("1").model == '1310'
    assert repository.read('1').an_achizitie == 2000
    assert repository.read('1').nr_km == 153455.42
    repository.delete("1")
    assert len(repository.read()) == 0


def test_customer_card_file_repository():
    filename = "test_customer_cards.json"
    clear_file(filename)
    repository = JsonRepository(filename)
    repository.create(CustomerCard('300', 'Popescu', 'Dan', 5011211330233,
                                   datetime.date(2001, 5, 18),
                                   datetime.date(2020, 8, 19)))
    assert len(repository.read()) == 1
    assert repository.read("300").nume == 'Popescu'
    assert repository.read('300').prenume == 'Dan'
    assert repository.read("300").CNP == 5011211330233
    repository.update(CustomerCard
                      ('300', 'Popescu', 'Ionut', 5001211330283,
                       datetime.date(2000, 5, 18),
                       datetime.date(2020, 8, 19)))
    assert repository.read("300").nume == 'Popescu'
    assert repository.read('300').prenume == 'Ionut'
    assert repository.read("300").CNP == 5001211330283
    repository.delete("300")
    assert len(repository.read()) == 0


def test_transaction_file_repository():
    filename = 'test_transaction.json'
    clear_file(filename)
    repository = JsonRepository(filename)
    repository.create(Transaction('100', '1', 'null', 250, 100,
                                  datetime.datetime(2021, 11, 15, 12, 24, 48),
                                  0, 0))
    assert len(repository.read()) == 1
    assert repository.read("100").id_car == '1'
    assert repository.read("100").id_customer_card == 'null'
    assert repository.read("100").suma_piese == 250
    assert repository.read("100").dateandtime == \
           datetime.datetime(2021, 11, 15, 12, 24, 48)
    repository.update(Transaction('100', '1', '55', 230, 45,
                                  datetime.datetime(2020, 1, 18, 8, 14, 3),
                                  0, 0))
    assert repository.read("100").id_car == '1'
    assert repository.read("100").id_customer_card == "55"
    assert repository.read("100").suma_piese == 230
    assert repository.read("100").dateandtime == \
           datetime.datetime(2020, 1, 18, 8, 14, 3)
    repository.delete("100")
    assert len(repository.read()) == 0


def test_car_repository():
    repository = RepositoryInMemory()
    repository.create(Car('1', 'Logan', 2005, 205467.12, 'nu'))
    assert len(repository.read()) == 1
    assert repository.read("1").model == 'Logan'
    assert repository.read('1').an_achizitie == 2005
    assert repository.read('1').nr_km == 205467.12
    repository.update(Car('1', '1310', 2000, 153455.42, 'nu'))
    assert repository.read("1").model == '1310'
    assert repository.read('1').an_achizitie == 2000
    assert repository.read('1').nr_km == 153455.42
    repository.delete("1")
    assert len(repository.read()) == 0


def test_customer_card_repository():
    repository = RepositoryInMemory()
    repository.create(CustomerCard('300', 'Popescu', 'Dan', 5011211330233,
                                   datetime.date(2001, 5, 18),
                                   datetime.date(2020, 8, 19)))
    assert len(repository.read()) == 1
    assert repository.read("300").nume == 'Popescu'
    assert repository.read('300').prenume == 'Dan'
    assert repository.read("300").CNP == 5011211330233
    repository.update(CustomerCard
                      ('300', 'Popescu', 'Ionut', 5001211330283,
                       datetime.date(2000, 5, 18),
                       datetime.date(2020, 8, 19)))
    assert repository.read("300").nume == 'Popescu'
    assert repository.read('300').prenume == 'Ionut'
    assert repository.read("300").CNP == 5001211330283
    repository.delete("300")
    assert len(repository.read()) == 0


def test_transaction_repository():
    repository = RepositoryInMemory()
    repository.create(Transaction('100', '1', 'null', 250, 100,
                                  datetime.datetime(2021, 11, 15, 12, 24, 48),
                                  0, 0))
    assert len(repository.read()) == 1
    assert repository.read("100").id_car == '1'
    assert repository.read("100").id_customer_card == 'null'
    assert repository.read("100").suma_piese == 250
    assert repository.read("100").dateandtime == \
           datetime.datetime(2021, 11, 15, 12, 24, 48)
    repository.update(Transaction('100', '1', '55', 230, 45,
                                  datetime.datetime(2020, 1, 18, 8, 14, 3),
                                  0, 0))
    assert repository.read("100").id_car == '1'
    assert repository.read("100").id_customer_card == "55"
    assert repository.read("100").suma_piese == 230
    assert repository.read("100").dateandtime == \
           datetime.datetime(2020, 1, 18, 8, 14, 3)
    repository.delete("100")
    assert len(repository.read()) == 0


def test_repository():
    test_car_repository()
    test_customer_card_repository()
    test_transaction_repository()
    test_transaction_file_repository()
    test_customer_card_file_repository()
    test_car_file_repository()
