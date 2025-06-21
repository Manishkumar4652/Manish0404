import random
import string
print('Welcome To Password Genrator!')
# user se input lenth lf password
lenths = int(input('Enter the password lenth: '))
# all characters set
characters = string.ascii_letters + string.digits + string.punctuation
# random password genrate
password = ''.join(random.choice(characters) for _ in range(lenths))
# print password
print('Generated Password:',password) 
print('Thanks For Using')