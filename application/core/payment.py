from .card import Card


class Payment(object):
    def __init__(self, credit_card_number, card_holder, exp_date,
            amount, security_code=None):
        self.card = Card(
            credit_card_number=credit_card_number,
            card_holder=card_holder,
            exp_date=exp_date,
            security_code=security_code
        )
        self.amount = amount
