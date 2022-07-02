import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def gen_cars(self):
        for i in range(10):
            if random.randint(1, 20) == 1:
                new_car = Turtle("square")
                new_car.penup()
                new_car.shapesize(stretch_wid=1, stretch_len=2)
                new_car.color(random.choice(COLORS))
                new_car.goto(280, random.randint(-260, 260))
                new_car.setheading(180)
                self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.speed)

    def collide(self, player):
        for car in self.cars:
            if car.distance(player) < 15:
                return True
        return False

    def increase_speed(self):
        self.speed += MOVE_INCREMENT
