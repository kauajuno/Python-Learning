# Create a letter using starting_letter.txt for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

with open("./Input/Names/invited_names.txt", mode='r') as names:
    name_list = names.readlines()
    name_list = [name.rstrip() for name in name_list]

with open("./Input/Letters/starting_letter.txt", mode='r') as original_letter:
    aux = original_letter.read()

for name in name_list:
    with open(f"./Output/ReadyToSend/{name}'s Letter.txt", mode='w') as individual_letter:
        individual_letter.write(aux.replace("[name]", name))