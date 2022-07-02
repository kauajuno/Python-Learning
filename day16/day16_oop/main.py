from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("darkviolet", "coral")
cont = 0

while cont < 40:
    timmy.forward(200)
    timmy.left(170)
    cont += 1

my_screen = Screen()
my_screen.exitonclick()
