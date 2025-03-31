

from random import randint
easy_level = 10
hard_level = 5

def check_answer (guess, answer, turns):
    if guess>answer:
        print("Too High")
        return turns - 1
    if guess<answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it hurray!! \nThe answer was: {answer}")

def set_difficulty():
    level = input("Choose difficulty level. Type 'hard' or 'easy': ")
    if level == 'easy':
        return easy_level
    if level == 'hard':
        return hard_level
    
def game():
    print("Welcome to the number guessing game")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)

    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number: ")

        guess = int(input("Make a guess: "))

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose!")
        elif guess != answer:
            print("Guess again")
    

game()
    