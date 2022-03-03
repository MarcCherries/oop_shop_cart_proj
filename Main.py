from Product import Product
from cart import ShoppingCart



new_product = Product('toothpaste', 3, 'hygiene')
print (new_product.price)

new_cart = ShoppingCart()

new_cart.subtotal(new_cart.contents)

new_cart.add_new_product(new_product.name)

print(new_cart.contents)

new_cart.subtotal(new_product.price)