import random

lowest_num=1
highest_num=100
answer=random.randint(lowest_num, highest_num)
guesses=0

is_running=True

print("----Python Number Guessing Game----")
while is_running:
    guess=input(f"Select a number between {lowest_num} and {highest_num}: ")

    if guess.isdigit():
        guess=int(guess)
        guesses+=1
        if guess<lowest_num or guess>highest_num:
            print(f"Please select a number between {lowest_num} and {highest_num}")
        elif guess< answer:
            print("TOO LOW")
        elif guess>answer:
            print("TOO HIGH")
        else:
            print(f"Correct The answer was {answer}")
            print(f"Total Number of guess is {guesses}")
            is_running=False
       
    
    else :
        print("Invalid input. Please enter a number.")