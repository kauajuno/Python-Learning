from turtle import Turtle, Screen
import random

turtle_colors = ["dark cyan", "aquamarine", "medium sea green", "lime", "gold", "crimson", "medium violet red",
                 "magenta", "dark violet", "medium slate blue", "blue", "pale green", "teal", "tomato", "orange red"]


def draw_square(turtle, size):
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)


def draw_dashed_line(turtle, size, interval):
    for i in range(size):
        turtle.forward(interval)
        turtle.pu()
        turtle.forward(interval)
        turtle.pd()


def draw_polygons(turtle, qtd):
    for polygon in range(3, qtd + 1):
        for _ in range(polygon):
            turtle.color(random.choice(turtle_colors))
            turtle.right(360/polygon)
            turtle.forward(100)


def random_walk(turtle, path_quantity):
    turtle.hideturtle()
    turtle.pensize(10)
    for _ in range(path_quantity):
        turtle.color((random.random(), random.random(), random.random()))
        turtle.right(random.randint(1, 4) * 90)
        turtle.forward(20)


def spirograph(turtle, quant):
    turtle.pensize(5)
    for _ in range(quant):
        turtle.color((random.random(), random.random(), random.random()))
        turtle.circle(50)
        turtle.right(360/quant)
        turtle.penup()
        turtle.forward(1)
        turtle.pendown()


timmy_turtle = Turtle()
my_screen = Screen()

timmy_turtle.shape("turtle")
timmy_turtle.color("purple", "medium sea green")
timmy_turtle.speed("fastest")

random_walk(timmy_turtle, 1000)

random_walk(timmy_turtle, 1000)


my_screen.exitonclick()
