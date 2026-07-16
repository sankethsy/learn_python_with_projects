#   *
#   ***
#  *****
# *******
# *******
#  *****
#   ***
#    *

# -------------
rows=int(input("enter : "))
symbol=input("enter symbol : ")

for x in range(1,rows+1) :
    for y in range(rows-x) :
        print(" ",end="")
    for z in range(2*x-1) :
        print(symbol,end="")
    print()

for x in range(rows,0,-1) :
    for y in range(rows-x) :
        print(" ",end="")
    for z in range(2*x-1) :
        print(symbol,end="")
    print()
    
