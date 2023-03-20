"""
You own a store.

Data:
List of products: prices, name, code, amounts, catagory
Amount of money

APIs:
add a new product
sell -> update amount of money made -> update if out of stock
"""

class Store:
    def print_greeting(self):
       print("welcome to the store")

    def __init__(self):
        print("New Store Initialized")
        self._profit = 0
        self._products = [{"name":"banana", "amount":3, "code": "12", "catagory": "fruit", "price":2},
                         {"name": "apple", "amount": 2, "code": "13", "catagory": "fruit", "price": 3},
                         {"name": "pear", "amount": 9, "code": "14", "catagory": "fruit", "price": 4},
                         {"name": "pumpkin", "amount": 12, "code": "15", "catagory": "vegetable", "price": 5}]

    def print_products(self):
        for product in self._products:
            print(product)

    def add_product(self, name, amount, code, catagory, price):
        product = {"name": name, "amount": amount, "code": code, "catagory": catagory, "price": price}
        self._products.append(product)

    def sell_product(self, name, amount_bought):
        for product in self._products:
            if product["name"] == name:
                product["amount"] -= amount_bought
                self._profit += product["price"]*amount_bought

    def _get_products_by_catagory(self, catagory):
        temp_list = []
        for product in self._products:
            if product["catagory"] == catagory:
                temp_list.append(product)

        return temp_list

    def apply_discount(self, catagory, discount):
        for product in self._get_products_by_catagory(catagory):
            product["price"] -= discount


my_store = Store()

my_store.add_product("hot dogs", 4, "20", "meat", 6)
my_store.sell_product("pumpkin", 3)
my_store.print_products()
print("____________________")
my_store.apply_discount("fruit", 1)
my_store.print_products()
