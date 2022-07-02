import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

hearts = 5
score = []
over = False

while not over:
    guess = input("Have a guess!\n").lower()
    for letter in chosen_word:
        if letter == guess:
            print("RIGHT!")
        else:
            print("WRONG!")
