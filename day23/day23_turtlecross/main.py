import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

car_manager = CarManager()

player = Player()
scoreboard = Scoreboard()

screen.onkey(player.move, "space")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.gen_cars()
    car_manager.move_cars()

    if player.won_level():
        scoreboard.update_scoreboard()
        car_manager.increase_speed()
        time.sleep(0.5)
        player.goto_start()
    if car_manager.collide(player):
        scoreboard.game_over()
        game_is_on = False

screen.exitonclick()
