rows=int(input("Enter the number of rows: "))
#takes the input from the user for the number of rows and converts it to an integer
coloums=int(input("Enter the number of coloums: "))
#takes the input from the user for the number of coloums and converts it to an integer
symbol=input("Enter the symbol: ")
#takes the input from the user for the symbol to be printed in the pattern

for x in range (rows) :
    for y in range (coloums) :
        print(symbol,end="")
    print()


#Enter the number of rows: 4
#Enter the number of coloums: 4
#Enter the symbol: @
# @@@@
# @@@@
# @@@@
# @@@@