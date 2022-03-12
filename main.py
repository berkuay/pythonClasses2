"""from item import Item


item1 = Item("MyItem", 750)

#item1.price = 900
item1.apply_increment(0.2)
item1.apply_discount()

print(item1.connect())"""
from phone import Phone
item1 = Phone("jscPhone", 1000,3)

item1.apply_discount()
print(item1.price)