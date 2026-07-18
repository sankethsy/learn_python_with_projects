Menu={"pizza":3.00,
      "nachos":4.50,
      "popcorn":6.00,
      "fries":2.50,
      "chips":1.00,
      "pretzel":3.50,
      "soda":3.00,
      "lemonade":4.5}

Cart=[]
Total=0

print("---------------MENU-------------")
for key,value in Menu.items():
    print(f"{key:10}:{value:.2f}")
print("---------------------------------")



while True:
    food=input("Select an item ( q to quit): ").lower()
    if food=="q":
        break
    elif Menu.get(food) is None :
        print("Select the Items from The MENU Only.")
    else :
      Cart.append(food)


print("-------------YOUR ORDER----------")

for food in Cart:
    Total+=Menu.get(food)
    print(food,end=" ")

print()
print(f"YOUR TOTAL BILL IS :${Total}")