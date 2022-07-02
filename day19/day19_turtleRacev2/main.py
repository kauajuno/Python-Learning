from turtle import Turtle, Screen


sc = Screen()

for i in range(6):
    tim = Turtle()
    tim.goto(x=-200, y=200-60*i)

sc.exitonclick()
