#this is going to be the main menu
#will have each cipher solver in a new folder
import sys
import time

print('Welcome!\n')
response = int(input("Please choose what cipher you would like to use: \n1) Caesar Cipher\n"))

if response == 1:
    import CeasarCipher


print('Thank you and have a good day!')
time.sleep(3)
