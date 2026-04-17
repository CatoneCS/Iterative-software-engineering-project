from flask import Flask, request, jsonify

from repository.product_repo import ProductRepository
from repository.order_repo import OrderRepository

from services.product_service import ProductService
from services.order_services import OrderService

app = Flask(__name__)

product_repo = ProductRepository()
order_repo = OrderRepository()

product_service = ProductService(product_repo)
order_service = OrderService(order_repo, product_repo)

def load_sample_data():

    product_service.create_product(1, "Mug", 12.50)
    product_service.create_product(2, "Scarf", 25.00)

    order_service.create_order(101)

    order_service.add_item_to_order(101, 1, 2)
    order_service.add_item_to_order(101, 2, 1)

load_sample_data()

@app.route("/products", methods=["GET"])
def get_products():

    products = product_service.list_products()

    response = []

    for product in products:
        response.append({
            "id": product.product_id,
            "name": product.name,
            "price": product.price,
        })
    return jsonify(response)


@app.route("/orders/<int:order_id>", methods =["GET"])
def get_order(order_id):

    order = order_service.get_order(order_id)

    if order is None:
        return jsonify({"error": "Order not found"}), 404
    items = []

    for item in order.items:
        items.append({
            "product": item.product.name,
            "quantity": item.quantity,
            "subtotal": item.get_subtotal()
        })
    return jsonify({
        "order_id": order.order_id,
        "items": items,
        "total": order.get_total(),
    })

if __name__ == "__main__":
    app.run(debug=True)