alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def shift_letter(letter, shift):
    if letter == ' ':
        return letter
    return alphabet[(alphabet.find(letter) + shift) % 26]

def caesar_cipher(message, shift):
    x = ''
    for i in message:
        x += shift_letter(i, shift)
    return x

def shift_by_letter(letter, letter_shift):
    if letter == ' ':
        return letter
    return alphabet[(alphabet.find(letter) + alphabet.find(letter_shift)) % 26]

def vigenere_cipher(message, key):
    index = 0

    x = ''
    for i in message:
        x += shift_by_letter(i, key[index % len(key)])
        index += 1
    return x

def scytale_cipher(message, shift):
    while len(message) % shift != 0:
        message += '_'
    
    x = ''
    for i in range(len(message)):
        index = (i // shift) + (len(message) // shift) * (i % shift)
        x += message[index]

    return x

def scytale_decipher(message, shift):
    text = ''

    index = (i % (len(message) // shift)) * shift + (i // len(message) // shift)
    for i in range(len(message)):
        text += message(index)
    
    return text 