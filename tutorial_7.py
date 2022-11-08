class Item:
    def __init__(self, item_name, item_quantity, item_price):
        self.name = item_name
        self.quantity = item_quantity
        self.price = item_price

        # print("Hey I have been created ")
    # def calc_discount (self, x, y):
    #     return x * y


# phone = Item()
# phone.name = "Techno spark"
# phone.version = 12
# phone.price = 2000
#
# earphones = Item()
# earphones.price = 1000

car = Item("Toyota", 20, 10000)
# gun = Item()
# print(type(phone))
# print(f' name of the phone is {phone.name} its of version {phone.version} and it costs Shs. {phone.price}. ')
# print(phone.calc_discount(0.8, phone.price))
# print(earphones.calc_discount(0.8, earphones.price))
print(f" hey my name is {item_name} there are {item_quantity} and the cost is {item_price}")
