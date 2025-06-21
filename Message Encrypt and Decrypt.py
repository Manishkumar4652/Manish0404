# Enter your simble to use in code
SYMBOL = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# make a infinit loop
# Choose option e and d
while True:
    print('DO you want to (e)encrypt and (d)decrypting')
    response = input('> ').lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break

    elif response.startswith('d'):
        mode = 'decrypt'
        break
    print('Please enter the letter e or d')

# Choose key for creat your password
while True:
    maxkey = len(SYMBOL) - 1
    print('Please enter the key (0 to {}) to use.'.format(maxkey))
    response = input('> ').upper()
    if not response.isdecimal():
        continue
    if 0 <= int(response) < len(SYMBOL):
        key = int(response)
        break

# Enter your message
print('Enter the message to {}.'.format(mode))
message = input('> ')
message = message.upper()

# code modifying Encrypt/Decrypt
translated = ''
for symbol in message:
    if symbol in SYMBOL:
        num = SYMBOL.find(symbol)
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key

        if num >= len(SYMBOL):
            num = num - len(SYMBOL)
        elif num < 0:
            num = num + len(SYMBOL)

        translated = translated + SYMBOL[num]

    else:
        translated = translated + symbol        

# Output reselt
print(translated)        

