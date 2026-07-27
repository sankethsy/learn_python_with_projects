import random

words = ("apple", "orange", "banana", "cocont", "pineapple")

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
    pass

def display_hint(hint):
    pass

def dispaly_ans(answer):
    pass

def main():
    answer=random.choice(words)
    hint=["_"]*len(answer)
    print(hint)





if __name__=="__main__":
 main()