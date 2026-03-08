from random_word import RandomWords
from itertools import cycle

words = RandomWords()


def encrypt(phrase):
    key = words.get_random_word()
    key = key.upper()
    key_index = 0
    encrypted_phrase = ''


    for char in phrase:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 65

            ascii_base = 65 if char.isupper() else 97
            new_char = chr((ord(char) - ascii_base + shift) % 26 + ascii_base)

            encrypted_phrase += new_char
            key_index = key_index + 1

        else:
            encrypted_phrase += char

    return encrypted_phrase



if __name__ == '__main__':
    phrase = input("Enter a phrase: ")
    encrypted_phrase = encrypt(phrase)
    print(encrypted_phrase)