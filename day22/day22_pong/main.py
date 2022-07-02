from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Pong")
screen.listen()
screen.tracer(0)

player1 = Paddle(1)
player2 = Paddle(2)
ball = Ball()
scoreboard = Scoreboard()

screen.onkey(player1.move_up, 'w')
screen.onkey(player1.move_down, 's')
screen.onkey(player2.move_up, 'Up')
screen.onkey(player2.move_down, 'Down')

game_is_on = True
speed = 0.05

while game_is_on:
    screen.update()
    time.sleep(speed)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if (ball.xcor() > 240 and ball.distance(player2) < 50) or (ball.xcor() < -240 and ball.distance(player1) < 50):
        ball.bounce_x()
    elif ball.xcor() > 250:
        scoreboard.update(1)
        time.sleep(0.5)
        ball.reset()
    elif ball.xcor() < -250:
        scoreboard.update(2)
        time.sleep(0.5)
        ball.reset()

screen.exitonclick()
