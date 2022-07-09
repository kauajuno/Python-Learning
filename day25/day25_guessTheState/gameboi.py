from turtle import Turtle


class Gameboi(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def show_state(self, state_name, position):
        self.goto(position)
        self.write(state_name, align="center", font=("Courier", 10, "normal"))
