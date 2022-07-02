import random
from db import database
from question import Question


def random_question():
    return random.choice(quiz)


def check_answer(actual_answer, user_guess):
    if user_guess == 'True':
        user_guess = True
    elif user_guess == 'False':
        user_guess = False
    if actual_answer == user_guess:
        print("That's right!")
        return True
    return False


quiz = list(database)
is_on = True

while is_on:
    random_q = random_question()
    current_question = Question(random_q, database[random_q])
    user_answer = input(f"{current_question.question} ").title()
    if not check_answer(current_question.answer, user_answer):
        is_on = False
