#     *
#    **
#   ***
#  ****
# *****
rows=int(input("Enter the number of rows: "))
#takes the input from the user for the number of rows and converts it to an integer
symbol=input("Enter the symbol: ")
#takes the input from the user for the symbol to be printed in the pattern

for x in range (1,rows+1) :
    #print spaces
    for y in range(rows-x):
        print(" ", end="")
    for z in range (x):
        print(symbol,end="")
    print()
    

    