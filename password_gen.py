import random

print ('Welcome To Your Password Generator')

chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*0123456789'

number = input ('Amount of passwords to be generated: ')
number = int(number)

length = input('Your password lenght is: ')
length = int(length)

print ('\nhere are your passwords:')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)
