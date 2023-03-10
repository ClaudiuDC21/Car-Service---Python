import datetime

from Repository.jsonRepository import JsonRepository
from Service.carService import CarService
from Service.customerCardService import CustomerCardService
from Service.transactionService import TransactionService


class Console:
    def __init__(self, car_service: CarService,
                 customer_card_service: CustomerCardService,
                 transaction_service: TransactionService,
                 car_repository: JsonRepository):
        self.car_service = car_service
        self.customer_card_service = customer_card_service
        self.transaction_service = transaction_service
        self.car_repository = car_repository

    def show_menu(self):
        print('a[car/crd/trz] - add masina, card client sau tranzactie. ')
        print('u[car/crd/trz] - update masina, card client sau tranzactie. ')
        print('d[car/crd/trz] - delete masina, card client sau tranzactie. ')
        print('s[car/crd/trz] - show all masina, card client sau tranzactie. ')
        print('4. Cautare masini si clienti. Cautare full text. ')
        print('5. Afisarea tuturor tranzactiilor cu '
              'suma cuprinsa intr-un interval dat.')
        print('6. Afișarea mașinilor ordonate descrescător după '
              'suma obținută pe manoperă. ')
        print('7. Afișarea cardurilor client ordonate descrescător după'
              ' valoarea reducerilor obținute')
        print('8. Ștergerea tuturor tranzacțiilor dintr-un anumit '
              'interval de zile.')
        print('9. Actualizarea garanției la fiecare mașină: o mașină este în'
              ' garanție dacă și numai dacă are maxim 3 ani de la achiziție și'
              ' maxim 60 000 de km.')
        print("s. Steregerea in cascada. ")
        print('n. Generarea de n valori random. ')
        print('x. Iesire')

    def read_date(self):
        try:
            date_str = input(
                'Dati data cu elemntele separate printr-un punct: ')
            date = date_str.split('.')
            year = int(date[2])
            month = int(date[1])
            day = int(date[0])
            return datetime.date(year, month, day)

        except ValueError as ve:
            print(f'Eroare: {ve}')
            return None

    def run_console(self):
        while True:
            self.show_menu()
            optiune = input('Alegeti o optiune: ')
            if optiune == 'acar':
                self.handle_add_car()
            elif optiune == 'ucar':
                self.handle_update_car()
            elif optiune == 'dcar':
                self.handle_delete_car()
            elif optiune == 'scar':
                self.handle_show_all(self.car_service.get_all())
            elif optiune == 'acrd':
                self.handle_add_customer_card()
            elif optiune == 'ucrd':
                self.handle_update_customer_card()
            elif optiune == 'dcrd':
                self.handle_delete_customer_card()
            elif optiune == 'scrd':
                self.handle_show_all(self.customer_card_service.get_all())
            elif optiune == 'atrz':
                self.handle_add_transaction()
            elif optiune == 'utrz':
                self.handle_update_transaction()
            elif optiune == 'dtrz':
                self.handle_delete_transaction()
            elif optiune == 'strz':
                self.handle_show_all(self.transaction_service.get_all())
            elif optiune == '4':
                self.ui_full_test_serch()
            elif optiune == '5':
                self.handle_show_tranzactions()
            elif optiune == '6':
                self.handle_shiw_cars_descending_after_suma_manopera()
            elif optiune == '7':
                self.handle_show_customer_card_descending_after_sales()
            elif optiune == '9':
                self.handle_update_waranty_at_all_cars()
            elif optiune == '8':
                self.handle_delete_transactions_in_interval()
            elif optiune == 'n':
                self.get_n_random_values_console()
            elif optiune == 'dallcar':
                self.handle_delete_all_cars()
            elif optiune == "s":
                self.handle_cascade_delete()
            elif optiune == 'x':
                break
            else:
                print('Optiune invalida, incercati din nou! ')

    def handle_add_car(self):
        try:
            id_car = input('Dati id-ul masinii: ')
            model = input('Dati modelul masinii: ')
            an_achizitie = int(input('Dati anul achizitiei masinii: '))
            nr_km = float(input('Dati numarul de kilometrii al masinii: '))
            in_garantie = input('Este masina in garantie! ( da / nu ): ')
            self.car_service.add_car(id_car, model, an_achizitie, nr_km,
                                     in_garantie)
        except ValueError as ve:
            print(f'Eroare de valodare: {ve}')
        except KeyError as ke:
            print(f'Eroare de id: {ke}')
        except Exception as ex:
            print(f'Eroare: {ex}')

    def handle_show_all(self, object):
        for obj in object:
            print(str(obj))

    def handle_add_customer_card(self):
        try:
            id_customer_card = input('Dati id-ul cardului de client: ')
            nume = input('Dati numele clientului: ')
            prenume = input('Dati prenumele clientului: ')
            CNP = int(input('Dati CNP-ul clientului: '))
            print('Introduceti data nasterii: ')
            data_nasterii = self.read_date()
            print('Introduceti data inregistrarii: ')
            data_inregistrari = self.read_date()
            self.customer_card_service.add_customer_card(id_customer_card,
                                                         nume, prenume, CNP,
                                                         data_nasterii,
                                                         data_inregistrari)
        except ValueError as ve:
            print(f'Eroare de valodare: {ve}')
        except KeyError as ke:
            print(f'Eroare de id: {ke}')
        except Exception as ex:
            print(f'Eroare: {ex}')

    def handle_add_transaction(self):
        try:
            id_entity = input('Dati id-ul tranzactiei: ')
            id_masina = input('Dati id-ul masinii: ')
            id_customer_card = input('Dati id-ul cardului de client: ')
            suma_piese = float(input('Dati suma pieselor: '))
            suma_manopera = float(input('Dati suma manoperei: '))
            total = 0
            sale = 0
            dateandtime_str = input('Dati data si ora tranzactiei de '
                                    'forma: (dd.mm.yyyy HH:MM:SS): ')
            dateandtime = self.read_dateandtime(dateandtime_str)
            self.transaction_service.add_transaction(id_entity, id_masina,
                                                     id_customer_card,
                                                     suma_piese,
                                                     suma_manopera,
                                                     dateandtime,
                                                     total, sale)

        except ValueError as ve:
            print(f'Eroare de validare: {ve}')
        except KeyError as ke:
            print(f'Eroare de id: {ke}')
        except Exception as ex:
            print(f'Eroare: {ex}')

    def handle_delete_transaction(self):
        try:
            id_transaction = input('Dati id-ul tranzactiei ce se va sterge: ')
            self.transaction_service.delete_transaction(id_transaction)
        except KeyError as ke:
            print(f'Eroare de id: {ke}')
        except Exception as ex:
            print(f'Eroare: {ex}')

    def handle_delete_car(self):
        try:
            id_car = input('Dati id-ul masinii ce se va sterge: ')
            self.car_service.delete_car(id_car)
        except KeyError as ke:
            print(f'Eroare de id: {ke}')
        except Exception as ex:
            print(f'Eroare: {ex}')

    def handle_delete_customer_card(self):
        try:
            id_customer_card = input(
                'Dati id-ul cardului de client ce se va sterge: ')
            self.customer_card_service.delete_customer_card(id_customer_card)
        except KeyError as ke:
            print(f'Eroare de id: {ke}')
        except Exception as ex:
            print(f'Eroare: {ex}')

    def handle_update_car(self):
        try:
            id_car = input('Dati id-ul masinii de modificat: ')
            model = input('Dati noul model al masinii: ')
            an_achizitie = int(input('Dati noul an al achizitiei masinii: '))
            nr_km = float(input('Dati noul numar de kilometrii al masinii: '))
            in_garantie = input(
                'Update - Este masina in garantie! ( da / nu ): ')
            self.car_service.update_car(id_car, model, an_achizitie, nr_km,
                                        in_garantie)
        except ValueError as ve:
            print(f'Eroare de valodare: {ve}')
        except KeyError as ke:
            print(f'Eroare de id: {ke}')
        except Exception as ex:
            print(f'Eroare: {ex}')

    def handle_update_customer_card(self):
        try:
            id_customer_card = input(
                'Dati id-ul cardului de client care se va modifica: ')
            nume = input('Dati noul nume al clientului: ')
            prenume = input('Dati noul prenume al clientului: ')
            CNP = int(input('Dati noul CNP al clientului: '))
            print('Introduceti noua data a nasterii: ')
            data_nasterii = self.read_date()
            print('Introduceti noua data a inregistrarii: ')
            data_inregistrari = self.read_date()
            self.customer_card_service.add_customer_card(id_customer_card,
                                                         nume, prenume, CNP,
                                                         data_nasterii,
                                                         data_inregistrari)
        except ValueError as ve:
            print(f'Eroare de valodare: {ve}')
        except KeyError as ke:
            print(f'Eroare de id: {ke}')
        except Exception as ex:
            print(f'Eroare: {ex}')

    def handle_update_transaction(self):
        try:
            id_transaction = input('Dati noul id al tranzactiei: ')
            id_masina = input('Dati noul id al masinii: ')
            id_customer_card = input('Dati noul id al cardului de client: ')
            suma_piese = float(input('Dati noua suma a pieselor: '))
            suma_manopera = float(input('Dati noua suma a manoperei: '))
            dateandtime_str = input('Dati noua data si ora a tranzactiei de '
                                    'forma: (dd.mm.yyyy HH:MM:SS): ')
            dateandtime = self.read_dateandtime(dateandtime_str)
            total = 0
            sale = 0
            self.transaction_service.update_transaction(id_transaction,
                                                        id_masina,
                                                        id_customer_card,
                                                        suma_piese,
                                                        suma_manopera,
                                                        dateandtime,
                                                        total, sale)
        except ValueError as ve:
            print(f'Eroare de validare: {ve}')
        except KeyError as ke:
            print(f'Eroare de id: {ke}')
        except Exception as ex:
            print(f'Eroare: {ex}')

    def handle_show_tranzactions(self):
        try:
            inceput_interval = float(input('Dati inceputul intervalului: '))
            sfarsit_interval = float(input('Dati sfarsitul intervalului: '))
            if inceput_interval <= sfarsit_interval:
                print(self.transaction_service.show_transactions_in_interval(
                    inceput_interval, sfarsit_interval))
            else:
                raise KeyError("Inceputul intervalului trebuie sa fie mai mic "
                               "sau egal decat sfarsitul intervalului.")
        except ValueError as ve:
            print(f'Eroare : {ve}')
        except KeyError as ke:
            print(f'Eroare : {ke}')
        except Exception as ex:
            print(f'Eroare: {ex}')

    def get_n_random_values_console(self):
        try:
            n = int(input('Dati numarul masinilor generate aleatoriu: '))
            self.car_service.get_n_random_values(n)
        except ValueError as ve:
            print(f'Eroare: {ve}')
        except KeyError as ke:
            print(f'Eroare: {ke}')
        except Exception as ex:
            print(f'Eroare: {ex}')

    def handle_delete_all_cars(self):
        for id_car in range(5, 1001):
            if self.car_repository.read(str(id_car)) is not None:
                self.car_service.delete_car(str(id_car))

    def ui_full_test_serch(self) -> None:
        search = input("Ce doriti sa cautati in lista: ")
        car_search = self.car_service.full_text_search_car(search)
        customer_card_search = self.customer_card_service. \
            full_text_search_customers(search)
        for car in car_search:
            print(car)
        for customer_card in customer_card_search:
            print(customer_card)

    def handle_delete_transactions_in_interval(self):
        try:
            print('Dati data de inceput a intervalului: ')
            begin_date = self.read_date()
            print('Dati data de sfarsit a intervalului: ')
            end_date = self.read_date()
            self.transaction_service.delete_all_tranzactions_on_some_days(
                begin_date, end_date)

        except ValueError as ve:
            print(f'Eroare: {ve}')
        except KeyError as ke:
            print(f'Eroare: {ke}')
        except Exception as ex:
            print(f'Eroare: {ex}')

    def handle_update_waranty_at_all_cars(self):
        try:
            self.car_service.update_waranty_on_every_car()
        except ValueError as ve:
            print(f'Eroare: {ve}')
        except KeyError as ke:
            print(f'Eroare: {ke}')
        except Exception as ex:
            print(f'Eroare: {ex}')

    def handle_show_customer_card_descending_after_sales(self):
        try:
            print(self.customer_card_service.
                  show_client_card_descending_after_sale())
        except ValueError as ve:
            print(f'Eroare: {ve}')
        except KeyError as ke:
            print(f'Eroare: {ke}')
        except Exception as ex:
            print(f'Eroare: {ex}')

    def handle_shiw_cars_descending_after_suma_manopera(self):
        try:
            print(self.car_service.show_cars_descending_by_suma_manopera())
        except ValueError as ve:
            print(f'Eroare: {ve}')
        except KeyError as ke:
            print(f'Eroare: {ke}')
        except Exception as ex:
            print(f'Eroare: {ex}')

    def read_dateandtime(self, dateandtime_str: str) -> datetime or None:
        try:
            dateandtime_str_split = dateandtime_str.split(" ")
            date_str = dateandtime_str_split[0]
            time_str = dateandtime_str_split[1]
            date_str_split = date_str.split(".")
            time_str_split = time_str.split(":")
            dd = int(date_str_split[0])
            mm = int(date_str_split[1])
            yyyy = int(date_str_split[2])
            HH = int(time_str_split[0])
            MM = int(time_str_split[1])
            SS = int(time_str_split[2])
            return datetime.datetime(yyyy, mm, dd, HH, MM, SS)
        except ValueError:
            return None

    def handle_cascade_delete(self):
        try:
            id_entity = input("Dati id-ul tranzactiei pentru stergerea "
                              "in cascada: ")
            self.transaction_service.cascade_delete(id_entity)
            print("Stergerea in cascada a fost efectuata cu succes! ")
        except ValueError as ve:
            print(f'Eroare: {ve}')
        except KeyError as ke:
            print(f'Eroare: {ke}')
        except Exception as ex:
            print(f'Eroare: {ex}')
