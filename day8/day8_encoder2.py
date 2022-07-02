def caesar(text_to_modify, shift_number, direction):
    cipher_text = ''
    if direction == 'decode':
        shift_number *= -1
    for letter in text_to_modify:
        position = alphabet.index(letter) + shift_number
        if position > len(alphabet) - 1:
            position = position % len(alphabet)
        cipher_text += alphabet[position]
    print(f"The {direction}d text is {cipher_text}")


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

flag = True

while flag is True:
    direction = input("What do you want to do? ").lower()
    if direction != 'encode' and direction != 'decode':
        flag = False
    else:
        text = input(f"What do you want to check? ").lower()
        number = int(input(f"What's the shift number? "))
        caesar(text, number, direction)
