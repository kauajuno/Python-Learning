from turtle import Turtle, Screen


def go_forward():
    timmy.forward(10)


timmy = Turtle()
my_screen = Screen()


my_screen.listen()
my_screen.onkey(go_forward, 'd')
my_screen.exitonclick()
