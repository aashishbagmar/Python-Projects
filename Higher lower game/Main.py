from art import logo, vs
from data import data
import random




def random_account():
    return random.choice(data)  

def format_Data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]

    return(f"{name}, a {description}, from {country}")

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'

def clear():
    print("\n" * 50)

def game():
    print(logo)
    current_score = 0
    game_continue = True

    a = random_account()
    b = random_account()


    while game_continue:
        a = b
        b = random_account()

        while a == b:
            b = random_account()

        print(f"Compare A: {format_Data(a)}")
        print(vs)
        print(f"Compare B: {format_Data(b)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_followers = a["follower_count"]
        b_followers = b["follower_count"]
        answer = check_answer(guess, a_followers, b_followers)

        clear()

        if answer :
            current_score += 1
            print(f"You're right! Current score: {current_score}.")
            
        else:
            game_continue = False
            print(f"You lose, Your current score is: {current_score}")


game()