from Product import Product
from Cart import ShoppingCart
from Customer import Customer

cust_one_cart = ShoppingCart()
product_one = Product ('Fancy Feast Tuna Dinner', 2, 'Pet Food' )
product_two = Product ('Frosted Mini Wheats', 4.5, 'Cereal')
product_three = Product ('Toothpaste', 3, 'Hygienic Items')
customer_name = input('Hello, please enter your name: \n')

customer_one = Customer(customer_name, cust_one_cart)

customer_one.add_to_cart(product_one)
customer_one.add_to_cart(product_two)
customer_one.add_to_cart(product_three)



print (customer_one.cart.contents)


customer_one.display_all_items_in_cart(cust_one_cart.contents)