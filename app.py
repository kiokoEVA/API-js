from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for products
products = []

# Product resource
class Product:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def to_dict(self):
        return {
            'name': self.name,
            'description': self.description,
            'price': self.price
        }

@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    
    # Validate input data
    if not data or 'name' not in data or 'description' not in data or 'price' not in data:
        return jsonify({'error': 'Invalid input data'}), 400
    
    try:
        product = Product(
            name=data['name'],
            description=data['description'],
            price=float(data['price'])
        )
        products.append(product)
        return jsonify(product.to_dict()), 201
    except ValueError:
        return jsonify({'error': 'Price must be a number'}), 400

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify([product.to_dict() for product in products]), 200

if __name__ == '__main__':
    app.run(debug=True)