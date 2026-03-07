#Just flips the alphabet completely backwards

def atBashCipher(text, encrypt=True):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    reversed_alphabet = alphabet[::-1]

    if encrypt:
        translation_table = str.maketrans(alphabet, reversed_alphabet)
        encoded_text = text.translate(translation_table)
        return encoded_text

    else:
        translation_table = str.maketrans(reversed_alphabet, alphabet)
        decoded_text = text.translate(translation_table)
        return decoded_text

class AtBashCipher():
    while True:
        reponse = int(input('Please make your choice: \n 1) Encode\n 2) Decode\n'))

        if reponse == 1:
            phrase = input('Please enter the phrase you would like to encode: ')
            phrase_encoded = atBashCipher(phrase)
            print(phrase_encoded)

        else:
            phrase = input('Please enter the phrase you would like to decode: ')
            phrase_decoded = atBashCipher(phrase, encrypt=False)
            print(phrase_decoded)

        reply = int(input('Would you like to do something else?\n 1) Yes\n 2) No\n '))
        if reply == 2:
            break