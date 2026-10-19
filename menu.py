class Menu:
    def __init__(self):
        pass

    def product(self):
        products = {
            1: {"name": "Product A", "price": 10.0},
            2: {"name": "Product B", "price": 15.0},
            3: {"name": "Product C", "price": 20.0},
        }
        return products


if __name__ == "__main__":
    menu = Menu()
    products = menu.product()
    for product_id, product_info in products.items():
        print(f"ID: {product_id}, Name: {product_info['name']}, Price: {product_info['price']}")