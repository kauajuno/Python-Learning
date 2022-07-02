from turtle import Turtle
import random

INIT_SIZE = 3
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in range(INIT_SIZE):
            new_segment = Turtle("square")
            new_segment.color((random.random(), random.random(), random.random()))
            new_segment.penup()
            new_segment.goto(-20 * i, 0)
            self.segments.append(new_segment)

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            self.segments[seg].goto(self.segments[seg - 1].pos())
        self.head.forward(MOVE_DISTANCE)

    def increase(self):
        new_segment = Turtle("square")
        new_segment.color((random.random(), random.random(), random.random()))
        new_segment.penup()
        new_segment.goto(1000, 1000)
        self.segments.append(new_segment)

    def body_collision(self):
        for seg in self.segments[1:]:
            if self.head.distance(seg) < 10:
                return True
        return False

    def wall_collision(self):
        return self.head.xcor() > 300 or self.head.xcor() < -300 or self.head.ycor() > 300 or self.head.ycor() < -300

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
