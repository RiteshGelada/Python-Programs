age = 23
txt = "I am Ritesh, and i am {}"
print(txt.format(age))

quantity = 45
itemno = 454
price = 50
myorder = "I want {} pieces of item {} for {} dollors"
print(myorder.format(quantity,itemno,price))


quantity = 45
itemno = 454
price = 50
myorder = "I want to pay {2} dollors for {0} pieces of tem {1}"
print(myorder.format(quantity,itemno,price))