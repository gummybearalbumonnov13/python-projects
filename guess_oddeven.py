# This is a Guess The Number game.
import random

guessesTaken = 0


print('Hello! What is your name?')
myName = input()

print('Would you like to choose from odd numbers or even numbers?')
oe = input()

if oe == 'odd':
    number = random.randrange(1, 50, 2)
    print('Well, ' + myName + ', I am thinking of an odd number between 1 and 50.')
    for guessesTaken in range(5):
        print('Take a guess.')
        guess = input()
        guess = int(guess)

        if guess < number:
            print('Your guess is too low.') #Eight spaces in front of "print"

        if guess > number:
            print('Your guess is too high.')

        if guess == number:
            break

    if guess == number:
        guessesTaken = str(guessesTaken + 1)
        print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')

    if guess != number:
        number = str(number)
        print('Nope. The number I was thinking of was ' + number + '.')

if oe == 'even':
    number = random.randrange(2, 50, 2)
    print('Well, ' + myName + ', I am thinking of an even number between 1 and 50.')

    for guessesTaken in range(5):
        print('Take a guess.')
        guess = input()
        guess = int(guess)

        if guess < number:
            print('Your guess is too low.') #Eight spaces in front of "print"

        if guess > number:
            print('Your guess is too high.')

        if guess == number:
            break

    if guess == number:
        guessesTaken = str(guessesTaken + 1)
        print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')

    if guess != number:
        number = str(number)
        print('Nope. The number I was thinking of was ' + number + '.')