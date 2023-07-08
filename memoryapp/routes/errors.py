from flask import jsonify

from memoryapp import app
from memoryapp.exceptions import NotFoundException


@app.errorhandler(NotFoundException)  # oczekuje do przekazania klase wyjątków
def handle_not_found(e: NotFoundException):
    return jsonify({'message': f'{e.item} not found'}), 404

