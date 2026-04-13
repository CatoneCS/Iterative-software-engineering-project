class Order:
    def __init__(self, order_id):
        self.order_id = order_id
        self.items = []
    def add_item(self, order_item):
        self.items.append(order_item)
    def get_total(self):
        total = 0
        for item in self.items:
            total += item.get_subtotal()
        return total
    def print_order_summary(self):
        print("Order Summary:")
        for item in self.items:
            print(f"{item.product.name} * {item.quantity} = ${item.get_subtotal():.2f}")
        print(f"Final Total: ${self.get_total():.2f}")