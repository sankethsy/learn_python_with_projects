# I am using list to store items in the shopping cart
Food=[]
Prices=[]
Total=0.0
while True :
    food=input("Enter the food to buy and 'q' to quit: ")
    if food=="q" or food =="Q" :
        break
    else:
        price=float(input(f"Enter the Price of a {food}: $ "))
        Food.append(food)
        Prices.append(price)

print("------------YOUR ITEMS ARE------------")

for food in Food :
    print(food,end=" ")
    

for Price in Prices :
    Total+=Price
    
print()
print(f"YOUR TOTAL ITEMS WORTH : ${Total:.2f}")
print("----------THANKYOU FOR VISITING------------")


