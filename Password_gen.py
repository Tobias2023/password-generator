import random
from django import *

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!?#$'

Password = input('Number of passwords?')
Password = int(Password)
length = input('Password length?')
length = int(length)

for p in range(Password):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)

