from repository.product_repo import ProductRepository
from repository.order_repo import OrderRepository

from services.product_service import ProductService
from services.order_services import OrderService


def main():

    product_repo = ProductRepository()
    order_repo =  OrderRepository()

    product_service = ProductService(product_repo)
    order_service = OrderService(order_repo, product_repo)

    product_service.create_product(1, "Mug", 12.50)
    product_service.create_product(2, "Scarf", 25.00)

    order_service.create_order(101)

    order_service.add_item_to_order(101,1,2)
    order_service.add_item_to_order(101,2,1)

    order = order_service.get_order(101)
    order.print_order_summary()


if __name__ == '__main__':
    main()