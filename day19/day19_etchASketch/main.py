from turtle import Turtle, Screen


def go_forwards():
    tim.forward(10)


def go_backwards():
    tim.back(10)


def rotate_clockwise():
    tim.right(10)


def rotate_c_clockwise():
    tim.left(10)


def clear_screen():
    tim.pu()
    tim.home()
    tim.clear()
    tim.pd()


tim = Turtle()
sc = Screen()
tim.color("purple", "pink")
tim.shape("triangle")

sc.listen()

sc.onkey(go_forwards, 'w')
sc.onkey(go_backwards, 's')
sc.onkey(rotate_clockwise, 'd')
sc.onkey(rotate_c_clockwise, 'a')
sc.onkey(clear_screen, 'c')

sc.exitonclick()
