#this is going to be the main menu
#will have each cipher solver in a new folder

import sys
import time

print('Welcome!\n')
while True:
    response = int(input("Please choose what cipher you would like to use: \n"
                         "1) Caesar Cipher\n"
                         "2) AtBash Cipher\n"
                         "3) Vigenere Cipher\n"
                         "4) A combination\n"))

    if response == 1:
        import CeasarCipher

        while True:
            response = int(input("Please make your choice:\n1) Encrypt message\n2) Decrypt message\n"))

            if response == 1:
                encrypted = input("Please enter the phrase you would like to encrypt: ")
                shift = int(input("Please enter the shift number: "))

                encrypted_text = CeasarCipher.encrypt(encrypted, shift)
                print(encrypted_text)

            elif response == 2:
                solve_it = input("Please enter the string that needs to be translated: ")
                shift_it = int(input("Please enter the shift number "))

                decrypted_text = CeasarCipher.decrypt(solve_it, shift_it, encrypt=False)
                print(decrypted_text)

            reply = int(input('Would you like to do something else?\n 1) Yes\n 2) No\n '))
            if reply == 2:
                break

    elif response == 2:
        import AtBashCipher

        while True:
            reponse = int(input('Please make your choice: \n 1) Encode\n 2) Decode\n'))

            if reponse == 1:
                phrase = input('Please enter the phrase you would like to encode: ')
                phrase_encoded = AtBashCipher.atBashCipher(phrase)
                print(phrase_encoded)

            else:
                phrase = input('Please enter the phrase you would like to decode: ')
                phrase_decoded = AtBashCipher.atBashCipher(phrase, encrypt=False)
                print(phrase_decoded)

            reply = int(input('Would you like to do something else?\n 1) Yes\n 2) No\n '))
            if reply == 2:
                break
    elif response == 3:
        import VigenereCipher

        while True:
            phrase = int(input('Please enter the phrase you would like to encode: '))
            phrase_encoded = VigenereCipher.encrypted_phrase(phrase)
            print(phrase_encoded)

            reply = int(input('Would you like to do something else?\n 1) Yes\n 2) No\n '))
            if reply == 2:
                break


    elif response == 4:
        import Mix

    reply = int(input('Would you like to use another cipher?\n 1) Yes\n 2) No\n'))
    if reply == 2:
        break


print('Thank you and have a good day!')
time.sleep(3)
