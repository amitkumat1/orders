class place_order:  
    from cart import Cart

    def __init__(self, order_id, customer_name):
        self.order_id = order_id
        self.customer_name = customer_name
        self.cart = self.Cart()

    def calculate_total(self):
        total = self.cart.get_total()
        return total

    def display_order(self):
        print(f"Order ID: {self.order_id}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Items:{self.cart.items}")
        for item in self.cart.items:
            print(f"- {item['name']}, Price: {item['price']})")
        print(f"Total: {self.calculate_total()}")


if __name__ == "__main__":
    order = place_order(order_id=1, customer_name="John Doe")
    order.cart.add_item(1)
    order.cart.add_item(2)
    order.cart.add_item(2)
    order.cart.remove_item(2)
    order.display_order()