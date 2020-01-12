from flask import Blueprint, jsonify, request, Response
from flask import current_app as app
import json

from .core.payment import Payment
from .core.payment_processor import PaymentProcessor
from .core.stock_processor import StockProcessor


main_bp = Blueprint('main_bp', __name__)


def validate_data(data):
    # check if data are ok

    if all(key in data.keys() 
            for key in ('credit_card_number', 'card_holder', 'exp_date')):
        return True, "Data valid"
    return False, "Invalid data"


@main_bp.route('/process_payment', methods=['POST'])
def process_payment():
    ok, message = validate_data(request.json)

    if not ok:
        return message, 400
    
    payment = Payment(**request.json)

    pp = PaymentProcessor()
    ok, message =  pp.process_payment(payment)

    if ok:
        return message, 200
    else:
        return message, 500

    
@main_bp.route('/estimate_price', methods=['POST'])
def estimate_price():
    data = request.json
    sp = StockProcessor(stock_file='dow_jones_index.data')
    sp.process_stock()
    return jsonify(sp.dataset.to_json())