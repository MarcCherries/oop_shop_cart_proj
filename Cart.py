from Product import Product

class ShoppingCart:
    def __init__(self):
        self.contents = []

        
    def subtotal(self, prices):
        sum_total = self.add_new_product(prices)

    def add_new_product(self, product_obj):
        self.contents.append(product_obj)

    def empty_shop_cart (self):
        self.contents = []





        

