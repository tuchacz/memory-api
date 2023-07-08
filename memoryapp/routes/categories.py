from flask import jsonify, request
from memoryapp import app
from memoryapp.repository import *


@app.route('/categories', methods=['GET'])
def categories():
    return jsonify(get_categories())


@app.route('/categories', methods=['POST'])
def add_category():
    r = request.json
    category_name = r['name']

    return jsonify(create_category(category_name)), 201
