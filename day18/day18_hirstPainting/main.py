import turtle
from turtle import Turtle, Screen
import random
import colorgen


def hirst_paint(t, size):
    t.penup()
    t.setpos(-200, -200)
    for dash in range(size):
        for _ in range(size):
            t.dot(20, random.choice(colors))
            t.forward(50)
        t.setpos(-200, (dash + 1) * 50 - 200)


colors = colorgen.color_gen()
turtle.colormode(255)

timmy_turtle = Turtle()
my_screen = Screen()

hirst_paint(timmy_turtle, 10)

my_screen.exitonclick()
