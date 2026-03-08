#codes a phrase with a random amount of ciphers that are on here.
# needs to only encode things, will make a detection file later

import random
import time

ciphernum = 3

class Mix():
    phrase = input('Please enter the phrase you would like to encrypt: ')


    print('Processing ...')
    time.sleep(2)
    random_stop = random.randint(1, ciphernum)
    num = 0

    while num < random_stop:
        choice = random.randint(1, ciphernum)

        if choice == 1:
            print("Caesar cipher")
            from CeasarCipher import encrypt
            shift = random.randint(1, 25)
            phrase = encrypt(phrase, shift)

        elif choice == 2:
            print("AtBash cipher")
            from AtBashCipher import atBashCipher
            phrase = atBashCipher(phrase)

        elif choice == 3:
            print("Vigenere cipher")
            from VigenereCipher import encrypt
            phrase = encrypt(phrase)

        num += 1

    print(phrase)