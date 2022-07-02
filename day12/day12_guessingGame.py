from random import randint

number = randint(1, 100)
lives = 5

print(f"I'm thinking about a number between 1 and 100")

while lives > 0:
    guess = int(input(f'Guess it! You have {lives} lives left\n'))
    if guess > number:
        print(f"Too high!")
    elif guess < number:
        print(f"Too low!")
    else:
        print(f"You won!")
        break
    lives -= 1
