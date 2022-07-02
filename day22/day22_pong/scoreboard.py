from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.p1_score = 0
        self.p2_score = 0
        self.write_score()

    def update(self, who_scored):
        if who_scored == 1:
            self.p1_score += 1
        else:
            self.p2_score += 1
        self.clear()
        self.write_score()

    def write_score(self):
        self.write(f"{self.p1_score} | {self.p2_score}", align="center", font=("Courier", 24, "normal"))
