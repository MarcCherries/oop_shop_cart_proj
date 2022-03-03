from Product import Product

class ShoppingCart:
    def __init__(self):
        self.contents = []
        
    def subtotal(self, contents):
        sum1 = sum(self.contents)
        print (sum1)

    def add_new_product(self, name):
        self.contents.append(name)




        

