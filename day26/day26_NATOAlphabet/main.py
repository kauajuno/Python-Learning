import pandas as pd

nato_csv = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {value.letter: value.code for (index, value) in nato_csv.iterrows()}

username = input("Tell us a name\n").upper()
result = [nato_dict.get(letter) for letter in username]
print(result)
