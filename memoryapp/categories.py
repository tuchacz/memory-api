from flask import jsonify
from memoryapp import app

# tworzenie listy kategori
categories_list = [
    {'category_id': 1, 'name': 'Dom'},
    {'category_id': 2, 'name': 'Rodzina'}
]


# jsonify zamienia liste w json
@app.route('/categories', methods=['GET'])
def categories():
    return jsonify(categories_list)
