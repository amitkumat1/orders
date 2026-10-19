class Cart:

    from menu import Menu
    
    def __init__(self):
        self.items = []
        self.menu = self.Menu()

    def add_item(self, item):
        products = self.menu.product()
        if item in products:
            self.items.append(products[item])

    def remove_item(self, item):
        products = self.menu.product()
        if item in products:
            product = products[item]
            if product in self.items:
                self.items.remove(product)

    def get_total(self):
        return sum(item["price"] for item in self.items)

    def clear_cart(self):
        self.items = []


if "__main__" == __name__:
    cart = Cart()
    cart.add_item(1)
    cart.add_item(2)
    cart.add_item(2)
    print("Items in cart:", cart.items)
    print("Total:", cart.get_total())
    cart.remove_item(2)
    print("Items in cart after removal:", cart.items)
    print("Total after removal:", cart.get_total())
    cart.clear_cart()
    print("Items in cart after clearing:", cart.items)