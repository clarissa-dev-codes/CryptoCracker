#this is going to be the main menu
#will have each cipher solver in a new folder

import CeasarCipher


def main():
    print("Welcome! Please pick the cipher you'd like to use:")
    response = int(input("1) Caesar Cipher\n"))

    if response == 1:
        CeasarCipher.CaesarCipher()
    else:
        print("That was not a valid choice")


if __name__ == "__main__":
    main()