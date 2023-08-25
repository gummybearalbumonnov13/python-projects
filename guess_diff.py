# This is a Guess The Number game.
import random

guessesTaken = 0


print('Hello! What is your name?')
myName = input()

print('What difficulty do you want to play? Choose from easy and hard.')
difficulty = input()

if difficulty == 'easy':
    number = random.randint(1, 50)
    print('Well, ' + myName + ', I am thinking of a number between 1 and 50.')
    for guessesTaken in range(10):
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

if difficulty == 'hard':
    number = random.randint(1, 100)
    print('Well, ' + myName + ', I am thinking of a number between 1 and 100.')

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