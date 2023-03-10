import datetime

from Domain.car import Car
from Domain.carValidator import CarValidator
from Domain.customerCard import CustomerCard
from Domain.customerCardValidator import CustomerCardValidator
from Domain.transactionValidator import TransactionValidator
from Repository.jsonRepository import JsonRepository
from Service.carService import CarService
from Service.customerCardService import CustomerCardService
from Service.transactionService import TransactionService
from utils import clear_file


def test_car_service():
    filename = "test_cars_service.json"
    clear_file(filename)
    car_repository = JsonRepository(filename)
    car_validator = CarValidator()
    filename = "test_transaction_service.json"
    clear_file(filename)
    transaction_repository = JsonRepository(filename)
    car_service = CarService(car_repository, car_validator,
                             transaction_repository)
    car_service.add_car("1", "E60", 1999, 203453.90, 'nu')
    assert len(car_service.get_all()) == 1
    assert car_repository.read("1").model == "E60"
    assert car_repository.read("1").an_achizitie == 1999
    car_service.delete_car("1")
    assert len(car_service.get_all()) == 0


def test_customer_card_service():
    filename = "test_customer_card_service.json"
    clear_file(filename)
    customer_card_validator = CustomerCardValidator()
    customer_card_repository = JsonRepository(filename)
    filename = "test_transaction_service.json"
    clear_file(filename)
    transaction_repository = JsonRepository(filename)
    customer_card_service = CustomerCardService(customer_card_repository,
                                                customer_card_validator,
                                                transaction_repository)
    customer_card_service.add_customer_card('300', 'Popescu', 'Dan',
                                            5011211330233,
                                            datetime.date(2001, 5, 18),
                                            datetime.date(2020, 8, 19))
    assert len(customer_card_service.get_all()) == 1
    customer_card_service.update_customer_card('300', 'Popescu', 'Stelian',
                                               5011211330233,
                                               datetime.date(1956, 5, 18),
                                               datetime.date(2020, 8, 19))
    assert customer_card_repository.read("300").nume == 'Popescu'
    assert customer_card_repository.read("300").prenume == 'Stelian'
    assert customer_card_repository.read("300").CNP == 5011211330233
    customer_card_service.delete_customer_card("300")
    assert len(customer_card_service.get_all()) == 0


def test_transaction_service():
    filename = "test_cars_service.json"
    clear_file(filename)
    car_repository = JsonRepository(filename)
    transaction_validator = TransactionValidator()
    filename = "test_transactions_service.json"
    clear_file(filename)
    transaction_repository = JsonRepository(filename)
    filename = "test_customer_card_service.json"
    clear_file(filename)
    customer_card_repository = JsonRepository(filename)
    transaction_service = TransactionService(transaction_repository,
                                             transaction_validator,
                                             car_repository,
                                             customer_card_repository)
    car_repository.create(Car('1', 'Logan', 2005, 205467.12, 'nu'))
    car_repository.create(Car('2', 'Focus', 2018, 20567.12, 'da'))
    customer_card_repository.create(
        CustomerCard('300', 'Popescu', 'Dan', 5011211330233,
                     datetime.date(2001, 5, 18),
                     datetime.date(2020, 8, 19)))
    customer_card_repository.create(
        CustomerCard('null', '', '', 5011211330233, datetime.date(2001, 5, 18),
                     datetime.date(2020, 8, 19)))
    transaction_service.add_transaction("500", "2", "300", 250, 100,
                                        datetime.datetime(2021, 11, 24,
                                                          13, 26, 1), 0, 0)
    assert len(transaction_service.get_all()) == 1
    assert transaction_repository.read("500").suma_piese == 0
    assert transaction_repository.read("500").dateandtime == \
           datetime.datetime(2021, 11, 24, 13, 26, 1)
    transaction_service.add_transaction("501", "1", "null", 400, 150,
                                        datetime.datetime(2020, 12, 4,
                                                          7, 39, 47), 0, 0)
    assert len(transaction_service.get_all()) == 2
    assert transaction_repository.read("501").suma_piese == 400
    assert transaction_repository.read("501").dateandtime == \
           datetime.datetime(2020, 12, 4, 7, 39, 47)
    begin_interval = 50
    end_interval = 300
    interval = transaction_service.show_transactions_in_interval(
        begin_interval, end_interval)
    assert len(interval) == 1
    transaction_service.delete_transaction("501")
    transaction_service.delete_transaction("500")
    car_repository.delete("1")
    car_repository.delete("2")
    customer_card_repository.delete("300")
    customer_card_repository.delete("null")


def test_service_functionalities():
    car_validator = CarValidator()
    customer_card_validator = CustomerCardValidator()
    transaction_validator = TransactionValidator()
    filename = "test_cars_service.json"
    clear_file(filename)
    car_repository = JsonRepository(filename)
    filename = "test_transaction_service.json"
    clear_file(filename)
    transaction_repository = JsonRepository(filename)
    filename = "test_customer_card_service.json"
    clear_file(filename)
    customer_card_repository = JsonRepository(filename)
    car_service = CarService(car_repository, car_validator,
                             transaction_repository)
    customer_card_service = CustomerCardService(customer_card_repository,
                                                customer_card_validator,
                                                transaction_repository)
    transaction_service = TransactionService(transaction_repository,
                                             transaction_validator,
                                             car_repository,
                                             customer_card_repository)
    # Cerinta 3.4
    car_service.add_car('1', 'Logan', 2005, 205467.12, 'nu')
    car_service.add_car('2', 'p1310', 2000, 153455.42, 'da')
    customer_card_service.add_customer_card('300', 'Popescu', 'Dan',
                                            5011211330233,
                                            datetime.date(2001, 5, 18),
                                            datetime.date(2020, 8, 19))
    customer_card_service.add_customer_card('301', 'Popica', 'Ionut',
                                            5001211330283,
                                            datetime.date(2000, 5, 18),
                                            datetime.date(2020, 8, 19))
    search = "p"
    car_res = car_service.full_text_search_car(search)
    customer_card_res = customer_card_service. \
        full_text_search_customers(search)
    assert len(car_res) == 1
    assert len(customer_card_res) == 2
    car_service.delete_car("1")
    car_service.delete_car("2")
    customer_card_service.delete_customer_card("300")
    customer_card_service.delete_customer_card("301")

    # Cerinta 3.5
    car_service.add_car('1', 'Logan', 2005, 205467.12, 'nu')
    car_service.add_car('2', 'p1310', 2000, 153455.42, 'da')
    customer_card_service.add_customer_card('300', 'Popescu', 'Dan',
                                            5011211330233,
                                            datetime.date(2001, 5, 18),
                                            datetime.date(2020, 8, 19))
    customer_card_service.add_customer_card('null', 'Popica', 'Ionut',
                                            5001211330283,
                                            datetime.date(2000, 5, 18),
                                            datetime.date(2020, 8, 19))
    transaction_service.add_transaction("500", "2", "300", 250, 1000,
                                        datetime.datetime(2021, 11, 24,
                                                          13, 26, 1), 0, 0)
    transaction_service.add_transaction("501", "1", "null", 400, 150,
                                        datetime.datetime(2020, 12, 4,
                                                          7, 39, 47), 0, 0)
    transaction_service.add_transaction("502", "2", "null", 40.34, 150.67,
                                        datetime.datetime(2020, 5, 12,
                                                          7, 35, 1), 0, 0)
    # begin_date = datetime.datetime(2020, 1, 1, 00, 00, 00)
    # end_date = datetime.datetime(2020, 12, 12, 23, 59, 59)
    begin_interval = 100
    end_interval = 700
    interval = transaction_service.show_transactions_in_interval(
        begin_interval, end_interval)
    assert len(interval) == 2
    car_service.delete_car("1")
    car_service.delete_car("2")
    customer_card_service.delete_customer_card("300")
    customer_card_service.delete_customer_card("null")
    transaction_service.delete_transaction("501")
    transaction_service.delete_transaction("502")
    transaction_service.delete_transaction("500")

    # Cerinta 3.6
    car_service.add_car('1', 'Logan', 2005, 205467.12, 'nu')
    car_service.add_car('2', 'p1310', 2000, 153455.42, 'da')
    customer_card_service.add_customer_card('300', 'Popescu', 'Dan',
                                            5011211330233,
                                            datetime.date(2001, 5, 18),
                                            datetime.date(2020, 8, 19))
    customer_card_service.add_customer_card('null', 'Popica', 'Ionut',
                                            5001211330283,
                                            datetime.date(2000, 5, 18),
                                            datetime.date(2020, 8, 19))
    transaction_service.add_transaction("500", "2", "300", 250, 1000,
                                        datetime.datetime(2021, 11, 24,
                                                          13, 26, 1), 0, 0)
    transaction_service.add_transaction("501", "1", "null", 400, 150,
                                        datetime.datetime(2020, 12, 4,
                                                          7, 39, 47), 0, 0)
    result = car_service.show_cars_descending_by_suma_manopera()
    assert result[0][0].model == 'p1310'
    assert result[0][0].an_achizitie == 2000
    car_service.delete_car("1")
    car_service.delete_car("2")
    customer_card_service.delete_customer_card("300")
    customer_card_service.delete_customer_card("null")
    transaction_service.delete_transaction("501")
    transaction_service.delete_transaction("500")

    # 3.7
    car_service.add_car('1', 'Logan', 2005, 205467.12, 'nu')
    car_service.add_car('2', 'p1310', 2000, 153455.42, 'da')
    customer_card_service.add_customer_card('300', 'Popescu', 'Dan',
                                            5011211330233,
                                            datetime.date(2001, 5, 18),
                                            datetime.date(2020, 8, 19))
    customer_card_service.add_customer_card('null', 'Popica', 'Ionut',
                                            5001211330283,
                                            datetime.date(2000, 5, 18),
                                            datetime.date(2020, 8, 19))
    transaction_service.add_transaction("500", "2", "300", 250, 1000,
                                        datetime.datetime(2021, 11, 24,
                                                          13, 26, 1), 0, 0)
    transaction_service.add_transaction("501", "1", "null", 400, 150,
                                        datetime.datetime(2020, 12, 4,
                                                          7, 39, 47), 0, 0)
    result = customer_card_service.show_client_card_descending_after_sale()
    assert result[0][0].nume == 'Popescu'
    assert result[0][0].CNP == 5011211330233
    car_service.delete_car("1")
    car_service.delete_car("2")
    customer_card_service.delete_customer_card("300")
    customer_card_service.delete_customer_card("null")
    transaction_service.delete_transaction("501")
    transaction_service.delete_transaction("500")

    # 3.8
    car_service.add_car('1', 'Logan', 2005, 205467.12, 'nu')
    car_service.add_car('2', 'p1310', 2000, 153455.42, 'da')
    customer_card_service.add_customer_card('300', 'Popescu', 'Dan',
                                            5011211330233,
                                            datetime.date(2001, 5, 18),
                                            datetime.date(2020, 8, 19))
    customer_card_service.add_customer_card('null', 'Popica', 'Ionut',
                                            5001211330283,
                                            datetime.date(2000, 5, 18),
                                            datetime.date(2020, 8, 19))
    transaction_service.add_transaction("500", "2", "300", 250, 1000,
                                        datetime.datetime(2021, 11, 24,
                                                          13, 26, 1), 0, 0)
    transaction_service.add_transaction("501", "1", "null", 400, 150,
                                        datetime.datetime(2020, 12, 4,
                                                          7, 39, 47), 0, 0)
    transaction_service.add_transaction("502", "1", "null", 400, 150,
                                        datetime.datetime(2020, 1, 14,
                                                          7, 39, 47), 0, 0)
    transaction_service.delete_all_tranzactions_on_some_days(
        datetime.datetime(2020, 1, 1, 00, 00, 00),
        datetime.datetime(2020, 12, 31, 23, 59, 59))
    assert len(transaction_service.get_all()) == 1
    assert transaction_service.get_all()[0].id_entity == "500"
    car_service.delete_car("1")
    car_service.delete_car("2")
    customer_card_service.delete_customer_card("300")
    customer_card_service.delete_customer_card("null")
    transaction_service.delete_transaction("500")

    # 1.9
    car_service.add_car('1', 'Logan', 2020, 25467.12, 'nu')
    car_service.add_car('2', 'p1310', 2000, 153455.42, 'da')
    car_service.add_car('3', "XC90", 2019, 12342.44, "nu")
    car_service.update_waranty_on_every_car()
    assert car_service.get_all()[0].in_garantie == "da"
    assert car_service.get_all()[2].in_garantie == "da"
    car_service.delete_car("1")
    car_service.delete_car("2")
    car_service.delete_car("3")


def test_service():
    test_car_service()
    test_customer_card_service()
    test_transaction_service()
    test_service_functionalities()
