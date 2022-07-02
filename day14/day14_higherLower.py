import random
from day14_art import logo


def random_famous():
    return random.choice(list(database))


def answer_check(a, b, user_answer):
    if database[a] > database[b]:
        right_answer = 'a'
    else:
        right_answer = 'b'
    if user_answer == right_answer:
        return True
    return False


database = {
    'Neymar': 174_000_000,
    'Cristiano': 446_000_000,
    'Kanye West': 16_000_000,
    'NMIXX': 2_200_000,
    'Stray Kids': 21_200_000,
    'Twice': 25_600_000,
    'Rihanna': 129_000_000,
    'Doja Cat': 23_900_000,
    'Arctic Monkeys': 3_300_000
}

should_stop = False

while should_stop is False:
    print(logo)

    # Setup
    score = 0
    contender1 = random_famous()
    contender2 = random_famous()
    while contender1 == contender2:
        contender2 = random_famous()

    alive = True

    while alive:
        answer = input(f"Who's the most famous: A: {contender1} or B: {contender2}?\n").lower()
        if answer_check(contender1, contender2, answer):
            score += 1
            print(f"That's right! Now your score is {score}")
            contender1 = contender2
            contender2 = random_famous()
            while contender1 == contender2:
                contender2 = random_famous()
        else:
            alive = False
            print(f"Game over! You ended with score {score}")

    if input(f"Press y to play again\n") != 'y':
        should_stop = True
