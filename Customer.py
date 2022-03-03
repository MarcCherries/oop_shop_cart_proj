from itertools import product
from Cart import ShoppingCart

class Customer:
    def __init__(self, name, cart):
        self.name = name
        self.cart = ShoppingCart()

    def add_to_cart(self, product_obj):
        self.cart.add_new_product(product_obj)
        
        
    def display_all_items_in_cart(self, contents):
        for self.item in contents:
            print(self.item)
        
        


