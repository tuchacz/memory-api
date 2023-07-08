from flask import jsonify, request
from memoryapp import app
from memoryapp.repository import *


@app.route('/categories/<int:category_id>/cards', methods=['GET'])
def cards(category_id):
    return jsonify(get_cards(category_id))


@app.route('/categories/<int:category_id>/cards', methods=['POST'])
def add_card(category_id):
    r = request.json

    word = r['word']
    translation = r['translation']

    return jsonify(create_card(category_id, word, translation)), 201


@app.route('/categories/<int:category_id>/cards/<int:card_id>', methods=['DELETE'])
def remove_card(category_id, card_id):
    delete_card(category_id, card_id)

    return '', 204
