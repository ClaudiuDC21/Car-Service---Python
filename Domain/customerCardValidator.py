from Domain.customerCard import CustomerCard
from Domain.customerCardErrors import CustomerCardError


class CustomerCardValidator:
    def validate(self, customer_card: CustomerCard):
        errors = []
        if customer_card.data_nasterii is None:
            errors.append("Data nasterii nu a fost introdusa corect. ")
        if customer_card.data_inregistrarii is None:
            errors.append("Data inregistrarii nu a fost introdusa corect. ")

        if len(errors) > 0:
            raise CustomerCardError(errors)
