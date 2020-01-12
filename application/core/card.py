
# card_schema = {
#     'type': 'object',
#     'properties': {
#         'credit_card_number': {
#                 "type": "string",
#                 "error_msg": "Please provide a credit card number"
#             },
#         'card_holder': {
#                 "type": "string",
#                 "error_msg": "Please provide the card holder"
#             },
#         'exp_date': {
#                 "type": "date",
#                 "error_msg": "Please provide an expiry date"
#             },
#         'security_code': {"type": "string"}
#     },
#     'required':['credit_card_number', 'card_holder', 'exp_date']
# }


class Card(object):
    def __init__(self, credit_card_number, card_holder, exp_date, security_code=None):
        self.credit_card_number = credit_card_number
        self.card_holder = card_holder
        self.exp_date = exp_date
        self.security_code = security_code


        