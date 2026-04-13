from domain.order import Order
from domain.order_item import OrderItem

class OrderService:

    def __init__(self, order_repo, product_repo):
        self.order_repo = order_repo
        self.product_repo = product_repo

    def create_order(self, order_id):
        order = Order(order_id)
        self.order_repo.save(order)
        return order

    def add_item_to_order(self, order_id, product_id, quantity):
        order = self.order_repo.get(order_id)
        product = self.product_repo.get(product_id)

        if order is None:
            raise ValueError("Order not found")
        if product is None:
            raise ValueError("Product not found")
        order_item = OrderItem(product, quantity)
        order.add_item(order_item)

        self.order_repo.save(order)

    def get_order(self, order_id):
        return self.order_repo.get(order_id)

    def list_orders(self):
        return self.order_repo.list_all()
