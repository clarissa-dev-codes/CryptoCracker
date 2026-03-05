def caesar(text, shift, encrypt=True):
    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = - shift

    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    encrypted_text = text.translate(translation_table)
    return encrypted_text


def encrypt(text, shift):
    return caesar(text, shift)


def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)


class CaesarCipher():
    while True:
        response = int(input("Please make your choice:\n1) Encrypt message\n2) Decrypt message\n"))

        if response == 1:
            encrypted = input("Please enter the phrase you would like to encrypt: ")
            shift = int(input("Please enter the shift number: "))

            encrypted_text = encrypt(encrypted, shift)
            print(encrypted_text)

        elif response == 2:
            solve_it = input("Please enter the string that needs to be translated: ")
            shift_it = int(input("Please enter the shift number "))

            decrypted_text = caesar(solve_it, shift_it, encrypt=False)
            print(decrypted_text)

        reply = int(input('Would you like to do something else?\n 1) Yes\n 2) No\n '))
        if reply == 2:
            print('\n')
            break



