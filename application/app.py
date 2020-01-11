from flask import Blueprint, jsonify
from flask import current_app as app

main_bp = Blueprint('main_bp', __name__)


@main_bp.route('/process_payment', methods=['GET'])
def process_payment():
    return jsonify({"asd": "Asd"})