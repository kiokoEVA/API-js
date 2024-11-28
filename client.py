import requests

API_URL = 'http://127.0.0.1:5000/products'

def add_product(name, description, price):
    product_data = {
        'name': name,
        'description': description,
        'price': price
    }
    response = requests.post(API_URL, json=product_data)
    if response.status_code == 201:
        print("Product created:", response.json())
    else:
        print("Failed to create product:", response.json())

def get_products():
    response = requests.get(API_URL)
    if response.status_code == 200:
        products = response.json()
        print("Products:")
        for product in products:
            print(product)
    else:
        print("Failed to retrieve products:", response.json())

if __name__ == '__main__':
    # Example usage
    add_product("Laptop", "A high-performance laptop", 999.99)
    add_product("Mouse", "Wireless mouse", 25.50)
    get_products()