import turtle
import pandas as pd
from gameboi import Gameboi

# TODO - Otherwise write the answer in the map

TOTAL_STATES = 51


def get_coordinates(df, right_answer):
    return int(df[df.state == right_answer].x), int(df[df.state == right_answer].y)


screen = turtle.Screen()
screen.title("U.S. guessing game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

gameboi = Gameboi()

game_data = pd.read_csv("50_states.csv")

game_is_on = True
current_score = 0
already_answered = []
states_list = game_data["state"].tolist()

while game_is_on:
    answer = screen.textinput("Guess a state", f"{current_score}/{TOTAL_STATES}").title()
    if answer not in already_answered and answer in states_list:
        current_score += 1
        already_answered.append(answer)
        gameboi.show_state(answer, get_coordinates(game_data, answer))

turtle.mainloop()
