import random
import time

def displayIntro():
    print('''You are in a land full of dragons. In front of you, you see two caves. In one cave, the dragon is friendly and will share his treasure with you. The other dragon is greedy and hungry, and will eat you on sight.''')
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you go into? ( 1 or 2)')
        cave = input()

    return cave

def checkCave(chosenCave):
    print('You approach the cave...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1,2)

    if chosenCave == str(friendlyCave):
        print('Gives you his trasure!')
        time.sleep(2)
        print('Will you be riding the dragon? (1 or 2)')
        ride = input()
        if ride == '1':
            print('You climb onto the dragon\'s back and it flies into the air.')
            time.sleep(1)
            print('In front of you are two paths diverged by a horde of birds. 1 will send you through peaceful airs, which the other will send you into a thunderstorm. Which path would you like to choose? (1 or 2)')
            path = input()
            peacefulAir = random.randint(1,2)
            if path == peacefulAir:
                print('You managed to get through the sky and managed to make it to the trading port! You sold all of your treasure and went back to live a lavish life.')
                time.sleep(2)
                print('The End!')
            else:
                print('You went into the thunderstorm. Your dragon was electrocuted out of the sky and you end up drowning in the sea.')
                time.sleep(2)
                print('The End.')
        if ride == '2':
            print('You refuse the offer and go back to your hometown.')
            time.sleep(2)
            print('The End!')
        if ride != '1' and ride != '2':
            print('Please select 1 or 2.')
            ride = input()
            if ride == '1':
                print('You climb onto the dragon\'s back and it flies into the air.')
                time.sleep(1)
                print('In front of you are two paths diverged by a horde of birds. 1 will send you through peaceful airs, which the other will send you into a thunderstorm. Which path would you like to choose? (1 or 2)')
                path = input()
                peacefulAir = random.randint(1,2)
                if path == peacefulAir:
                    print('You managed to get through the sky and managed to make it to the trading port! You sold all of your treasure and went back to live a lavish life.')
                    time.sleep(2)
                    print('The End!')
                else:
                    print('You went into the thunderstorm. Your dragon was electrocuted out of the sky and you end up drowning in the sea.')
                    time.sleep(2)
                    print('The End.')
            if ride == '2':
                print('You refuse the offer and go back to your hometown.')
                time.sleep(2)
                print('The End!')

    else:
        print('Gobbles you down in one bite!')


playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print('Do you want to play again? (yes or no)')
    playAgain = input()