from Domain.transactionErrors import TransactionError
from Domain.transaction import Transaction


class TransactionValidator:
    def validate(self, transaction: Transaction):
        errors = []
        if transaction.suma_piese < 0:
            errors.append('Suma pieselor trebuie sa fie un numar pozitiv. ')
        if transaction.suma_manopera < 0:
            errors.append('Suma manoperei trebuie sa fie un numar pozitiv.')
        if transaction.dateandtime is None:
            errors.append('Data trebuie sa fie introdusa corect. ')
        if len(errors) > 0:
            raise TransactionError(errors)
