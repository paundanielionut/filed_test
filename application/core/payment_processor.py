from flask import current_app as app


class PaymentGateway(object):
    def __init__(self, payment):
        self.payment = payment
        # this is a mock for the actual gateway api
        # normally I would check the availability using a request..
        self.available = True
    
    def check_availability(self):
        return self.available

    
    def do_payment(self):
        if self.check_availability():
            print("do payment")
            data = {
                "credit_card_number": self.payment.card.credit_card_number, 
                "card_holder": self.payment.card.card_holder, 
                "exp_date": self.payment.card.exp_date,
                "amount": self.payment.amount, 
                "security_code": self.payment.card.security_code
            }
            if app.db.insert(data):
                return True, "payment successful"
            else:
                return False, "payment not successful"
        else:
            return False, "gateway not available"


class PremiumPaymentGateway(PaymentGateway):
    def __init__(self, payment):
        super().__init__(payment)


class ExpensivePaymentGateway(PaymentGateway):
    def __init__(self, payment):
        super().__init__(payment)


class CheapPaymentGateway(PaymentGateway):
    def __init__(self, payment):
        super().__init__(payment)


class PaymentProcessor(object):
    # functionalities

    def process_payment(self, payment):
        if payment.amount <= 20:
            cheap_payment = CheapPaymentGateway(payment)
            return cheap_payment.do_payment()
        elif 21 <= payment.amount <= 500:
            expensive_payment = ExpensivePaymentGateway(payment)
            ok, message = expensive_payment.do_payment()
            if not ok:
                cheap_payment = CheapPaymentGateway(payment)
                return cheap_payment.do_payment()
            return ok, message
                
        elif payment.amount > 500:
            premium_payment = PremiumPaymentGateway(payment)
            ok, message = False, "Gateway not available"
            for i in range(3):
                ok, message = premium_payment.do_payment()
                if ok:
                    return ok, message
            return ok, message


