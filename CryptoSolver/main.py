#this is going to be the main menu
#will have each cipher solver in a new folder
import sys
import time

print('Welcome!\n')
while True:
    response = int(input("Please choose what cipher you would like to use: \n1) Caesar Cipher\n"))

    if response == 1:
        import CeasarCipher

    reply = int(input('Would you like to use another cipher?\n 1) Yes\n 2) No\n'))
    if reply == 2:
        print('\n')
        break


print('Thank you and have a good day!')
time.sleep(3)
