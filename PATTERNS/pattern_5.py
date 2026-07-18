# Rows: 5
# Symbol: #
#     #
#   #####
#  #######
# #########
rows = int(input("Rows: "))
symbol = input("Symbol: ")

for i in range(1, rows + 1):

    # Print spaces
    for j in range(rows-i):
        print(" ", end="")

    # Print stars
    for k in range(2*i-1):
        print(symbol, end="")

    print()

    #Inverted pyramid

# Rows: 5
# Symbol: #
# #########
#  #######
#   #####
#    ###
#     #

rows = int(input("Rows: "))
symbol = input("Symbol: ")

for i in range(rows,0,-1):

    # Print spaces
    for j in range(rows-i):
        print(" ", end="")

    # Print stars
    for k in range(2*i-1):
        print(symbol, end="")

    print()

