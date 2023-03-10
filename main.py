from Domain.carValidator import CarValidator
from Domain.customerCardValidator import CustomerCardValidator
from Domain.transactionValidator import TransactionValidator
from Repository.jsonRepository import JsonRepository
from Service.carService import CarService
from Service.customerCardService import CustomerCardService
from Service.transactionService import TransactionService
from Tests.allTests import test_all
from UserInterface.Console import Console




def main():
    car_repository = JsonRepository('cars.json')
    transaction_repository = JsonRepository('transasction.json')
    customer_card_repository = JsonRepository('customer_card.json')
    car_validator = CarValidator()
    car_service = CarService(car_repository, car_validator,
                             transaction_repository)

    customer_card_validator = CustomerCardValidator()
    customer_card_service = CustomerCardService(customer_card_repository,
                                                customer_card_validator,
                                                transaction_repository)

    transaction_validator = TransactionValidator()
    transaction_service = TransactionService(transaction_repository,
                                             transaction_validator,
                                             car_repository,
                                             customer_card_repository)

    console = Console(car_service, customer_card_service, transaction_service,
                      car_repository)
    console.run_console()


if __name__ == '__main__':
    test_all()
    main()
