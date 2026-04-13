from domain.product import Product

class ProductService:
    def __init__(self, product_repo):
        self.product_repo = product_repo

    def create_product(self, product_id, name, price):
        product = Product(product_id, name, price)
        self.product_repo.add(product)
        return product

    def get_product(self, product_id):
        return self.product_repo.get(product_id)

    def list_products(self):
        return self.product_repo.list_all()

