from flask import Flask, jsonify, request
import json
from flask_cors import CORS

app = Flask("Product Server")
CORS(app)


products = [
    {'id': 143, 'name': 'Notebook', 'price': 5.49},
    {'id': 144, 'name': 'Black Marker', 'price': 1.99}
]


# Add all the REST API end-points here

# GET request - http://localhost:5000/products
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)


# GET request - http://localhost:5000/product/144 - with method GET 
@app.route('/products/<id>', methods=['GET'])
def get_product(id):
    id = int(id)
    product = [x for x in products if x["id"] == id][0]
    return jsonify(product)


# POST request - http://localhost:5000/products - with method POST
@app.route('/products', methods=['POST'])
def add_product():
    products.append(request.get_json())
    return '', 201


# PUT Request - http://localhost:5000/products/144 - with PUT method
@app.route('/products/<id>', method=['PUT'])
def update_product(id):
    id = int(id)
    update_product = json.loads(request.data)
    product = [x for x in products if x["id"] == id][0]
    for key, value in update_product.items():
        product[key] = value
    return '', 204

# DELETE endpoint request - http://localhost:5000/products/144
@app.route('/products/<id>', methods=['DELETE'])
def remove_product(id):
    id = int(id)
    product = [x for x in products if x["id"] == id][0]
    products.remove(product)
    return '', 204

app.run(port=5000,debug=True)
