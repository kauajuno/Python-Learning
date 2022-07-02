from turtle import Turtle, Screen
import random


def somebody_won(t):
    if t.position()[0] > 390:
        return True
    return False


turtles = []
colors = ["red", "blue", "green", "yellow", "pink", "purple", "cyan"]
sc = Screen()
should_stop = False
winner = None

sc.setup(width=850, height=650)

for i in range(7):
    turtles.append(Turtle())
    turtles[i].shape("turtle")
    turtles[i].speed("normal")
    turtles[i].color(colors[i])
    turtles[i].setpos(x=-390, y=300 - i * 100)

user_bet = sc.textinput(title="Make your bet!", prompt="Which turtle will win the race? enter a color: ").lower()
user_bet = colors.index(user_bet)

while not should_stop:
    for i in range(7):
        turtles[i].forward(random.randint(10, 25))
        if somebody_won(turtles[i]) is True:
            should_stop = True
            winner = i
            break


if winner == user_bet:
    print("You win! Congratulations!")
else:
    print(f"You lose! The winner is {colors[winner]}")

sc.exitonclick()
