from turtle import Turtle

SIDE = 280


class Paddle(Turtle):

    def __init__(self, player_num):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        if player_num == 1:
            self.goto(-280, 0)
        else:
            self.goto(280, 0)

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - 20)


