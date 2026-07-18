# Tuple containing all quiz questions
questions=(("How many elements are  in the periodic table?"),
           ("Which Animal lays the Larget Egg?"),
           ("What is the most abundant gas in Earth's Atmosphere?"),
           ("How amy bones are in the Human Body"),
           ("Which Planet in the Solar System is the hottest"))

# Tuple containing the options for each question
options=(("A. 116 ","B. 117 ","C. 118","D. 119 "),
         ("A. Whale","B. crocodile","C. Elephat","D. Ostrich"),
         ("A. Nitrogen","B. Oxygen","C. Carbon-Dioxide","D. hydrogen"),
         ("A. 206","B. 207", "C. 208","D. 209"),
         ("A. Mercury","B. Venus","C. Earth","D. Mars "))

# Tuple containing the correct answers
answers=("C","D","A","A","B")

# List to store the user's guesses
guesses=[]

# Variable to keep track of the user's score
score=0

# Variable used to access the current question, options, and answer
question_num=0

# Loop through each question in the quiz
for question in questions:
    print("------------------------")
    print(question)

    # Display all options for the current question
    for option in options[question_num]:
        print(option)

    # Take the user's answer as input and convert it to uppercase
    guess=input("Enter (A,B,C,D) : ").upper()

    # Check whether the user's answer is correct
    if guess == answers[question_num]:
        score+=1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer""}")

    # Store the user's guess in the list
    guesses.append(guess)

    # Move to the next question
    question_num+=1

# Display the result section
print("-----------------------------------------------------")
print("                   RESULT                            ")
print("-----------------------------------------------------")

# Display the correct answers
print("answers",end=" ")
for ans in answers:
    print(ans,end=" ")
print()

# Display the user's guesses
print("guesses",end=" ")
for guess in guesses:
    print(guess,end=" ")
print()

# Calculate the score as a percentage
score=int(score/len(questions)*100)

# Display the final score
print(f"Your score is : {score}%")