# super class: User
# Attributes: name, email
# Methods: __init__, login, logout

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.logged_in = False

    def login(self):
        self.logged_in = True
        print(f"{self.email} has logged in.")
    
    def logout(self):
        self.logged_in = False
        print(f"{self.email} has logged out.")

#subclass Cashier
# Attributes: till_id
# Methods: make_order, process_payment

# subclass Customer
# Attributes: shopping_cart
# methods: order, complain

class Cashier(User):
    def __init__(self, name, email, till_id):
        super().__init__(name, email)
        self.till_id = till_id

    def make_order(self):
        print(f"{self.email} is making an order")

    def process_payment(self):
        print(f"{self.email} is making a payment")

class Customer(User):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.shopping_cart = []
        
    def addtocart(self, item):
        self.shopping_cart.append(item)

    def order(self):
        print(f"{self.email} is ordering.")

    def complain(self):
        print(f"{self.email} is complaining.")

name1 = "Timmy"
email1 = "tim@internship.com"
user1 = User(name1, email1)
# Test 1: create user
print(user1.__dict__)
user1.login()
user1.logout()

# Test 2: create customer
name2 = "Jimmy"
email2 = "jimmy@coolperson.com"
user2 = User(name2, email2)
customer2 = Customer(user2, email2)
print(customer2.__dict__)
customer2.login()
customer2.order()
customer2.addtocart("eggs")
customer2.addtocart("bacon")
print("shopping cart: ", customer2.shopping_cart)
customer2.complain()
customer2.logout()