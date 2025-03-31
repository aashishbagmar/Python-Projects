import turtle
import random
import colorgram
from turtle import Turtle, Screen

image = "image.jpeg"
rgb_color = []
colors = colorgram.extract(image, 30)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, b, b)
    rgb_color.append(new_color)

turtle.colormode(255)
color_list = [(248, 235, 235), (236, 243, 243), (251, 247, 247), (235, 250, 250), (227, 98, 98), (202, 109, 109), (118, 203, 203), (174, 101, 101), (165, 43, 43), (53, 147, 147), (11, 60, 60), (204, 176, 176), (158, 64, 64), (121, 161, 161), (206, 123, 123), (54, 124, 124), (172, 43, 43), (26, 145, 145), (17, 23, 23), (232, 194, 194), (54, 82, 82), (44, 13, 13), (62, 32, 32), (42, 185, 185), (146, 196, 196), (99, 195, 195), (140, 225, 225), (214, 59, 59), (172, 229, 229), (234, 159, 159)]
tim = turtle.Turtle()

tim.hideturtle()
tim.setheading(220)
tim.penup()
tim.forward(350)
tim.setheading(0)
no_of_dots = 100
tim.speed(0)

for count in range(1, no_of_dots):
    tim.dot(20,random.choice(color_list))
    tim.penup()
    tim.forward(50)

    if count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle.Screen()
screen.exitonclick()