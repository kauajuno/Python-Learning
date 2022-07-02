"""
This project uses inheritance, a concept introduced in day 21
"""

from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

INIT_SIZE = 3

sc = Screen()
sc.setup(width=600, height=600)
sc.bgcolor("black")
sc.title("My Snake Game")
sc.tracer(0)
sc.listen()

snake = Snake()
food = Food()
scoreboard = Scoreboard()

sc.onkey(snake.up, "Up")
sc.onkey(snake.down, "Down")
sc.onkey(snake.left, "Left")
sc.onkey(snake.right, "Right")

sc.onkey(snake.up, "Up")
sc.onkey(snake.down, "Down")
sc.onkey(snake.left, "Left")
sc.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    sc.update()
    time.sleep(0.05)
    snake.move()

    if snake.head.distance(food) < 15:
        food.realloc()
        snake.increase()
        scoreboard.update_score()

    if snake.wall_collision() or snake.body_collision():
        scoreboard.game_over()
        game_is_on = False

sc.exitonclick()
