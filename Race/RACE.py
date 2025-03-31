import turtle
from turtle import Turtle, Screen, setheading
import random


screen = Screen()
screen.setup(width=900, height=600)
user_bet = screen.textinput(title="Make your bet", prompt="Who will win the race?Choose a color: ")
is_game_on = False
colors = ["red", "orange", "yellow", "purple", "green", "blue"]
y_direction = [100, 60, 20, -20, -60, -100]
all_turtle = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape ="turtle")
    new_turtle.speed(0)
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-430, y=y_direction[turtle_index])
    all_turtle.append(new_turtle)
if user_bet:
    is_game_on = True

while is_game_on:


    for turtle in all_turtle:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

        if turtle.xcor() > 430:
            if turtle.pencolor() == user_bet:
                print(f"You win. {turtle.pencolor()} has won the match. ")
            else:
                print(f"You lose. {turtle.pencolor()} has won the match. ")

            is_game_on = False
