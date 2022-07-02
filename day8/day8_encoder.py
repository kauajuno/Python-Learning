def encrypt(text_uncrypted, shift_number):
    enc = ''
    for letter in text_uncrypted:
        if alphabet.index(letter) + shift_number > 25:
            enc += alphabet[alphabet.index(letter) + shift_number - 26]
        else:
            enc += alphabet[alphabet.index(letter) + shift_number]
    return enc


def decrypt(text_encrypted, shift_number):
    dec = ''
    for letter in text_encrypted:
        if alphabet.index(letter) - shift_number < 0:
            dec += alphabet[alphabet.index(letter) - shift_number + 26]
        else:
            dec += alphabet[alphabet.index(letter) - shift_number]
    return dec


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

flag = True

while flag is True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt, anything else to quit:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == 'encode':
        encrypted_text = encrypt(text, shift)
        print(f"The encrypted text is {encrypted_text}")
    elif direction == 'decode':
        decrypted_text = decrypt(text, shift)
        print(f"The decrypted text is {decrypted_text}")
    else:
        flag = False
