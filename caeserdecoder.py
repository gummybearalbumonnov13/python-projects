"""Caesar Cipher Hacker, by Al Sweigart al@inventwithpython.com This program hacks messages encrypted with the Caesar cipher by doing a brute force attack against every possible key. More info at: https://en.wikipedia.org/wiki/Caesar_cipher#Breaking_the_cipher View this code at https://nostarch.com/big-book-small-python-projects Tags: tiny, beginner, cryptography, math"""

print('Caesar Cipher Hacker, by Al Sweigart al@inventwithpython.com')

print('Enter the encrypted Caesar cipher message to hack.')
message = input('> ')

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(SYMBOLS)):
    translated = ''

    for symbol in message:
        if symbol in SYMBOLS:
            num = SYMBOLS.find(symbol)
            num = num - key

            if num < 0:
                num = num + len(SYMBOLS)

            translated = translated + SYMBOLS[num]
        else:
            translated = translated + symbol

    print('Key #{}: {}'.format(key, translated))

