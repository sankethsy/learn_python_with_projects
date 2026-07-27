import random
from hangman_game.words_list import words

# this is a dict of key:()
hangman = {
    0: ("   ",
        "   ",
        "   "),

    1: (" o ",
        "   ",
        "   "),

    2: (" o ",
        " | ",
        "   "),

    3: (" o ",
        "/| ",
        "   "),

    4: (" o ",
        "/|\\",
        "   "),

    5: (" o ",
        "/|\\",
        "/  "),

    6: (" o ",
        "/|\\",
        "/ \\")
}


def display_man(wrong_guess):
    for line in hangman[wrong_guess]:
       print(line)

def display_hint(hint):
    print(" ".join(hint))

def dispaly_ans(answer):
    print(" ".join(answer))

def main():
    answer=random.choice(words)
    hint=["_"]*len(answer)
    wrong_guess=0
    guessed_letetrs=set()

    is_running=True

    while is_running:
       display_man(wrong_guess)
       display_hint(hint)
       guess=input("Enter an Letter: ").lower()

       if len(guess) !=1 or not guess.isalpha():
           print("Invalid input")
           continue

       if guess in guessed_letetrs:
           print(f"{guess} is already guessed")

       guessed_letetrs.add(guess)

       if guess in answer:
            for i in range(len(answer)):
                if answer[i]==guess:
                    hint[i]=guess
       else :
           wrong_guess+=1
       if "_" not  in hint:
           display_man(wrong_guess)
           dispaly_ans(answer)
           print("YOU WIN")
           is_running=False
       elif wrong_guess>=len(hangman)-1:
           display_man(wrong_guess)
           dispaly_ans(answer)
           print("YOU LOOSE")
           is_running=False
           
            
if __name__=="__main__":
 main()