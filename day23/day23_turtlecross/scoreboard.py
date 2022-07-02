from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.color("black")
        self.hideturtle()
        self.goto(0, 270)
        self.write_scoreboard()

    def update_scoreboard(self):
        self.level += 1
        self.clear()
        self.write_scoreboard()

    def write_scoreboard(self):
        self.write(f"LEVEL: {self.level}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", align="center", font=FONT)
