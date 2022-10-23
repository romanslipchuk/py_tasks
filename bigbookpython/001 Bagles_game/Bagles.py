"""
Bagels game from book
"""

import random

NUM_DIGITS = 3  # number of digits to guess
MAX_GUESSES = 10  # number of guesses


def getSecretNum():
    # numbers = list('0123456789')  # creates list of numbers
    # random.shuffle(numbers)  # shuffle numbers list
    # take first 3 numbers to secretNum
    secretNum = '123'
    # for number in range(NUM_DIGITS):
    #     secretNum += str(numbers[number])
    return secretNum


def getClues(guess, secretNum):
    """Returns clues with phrases pico, fermi, bagels based on guess and secretNum values"""
    if guess == secretNum:
        return "BINGO!"

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
              # correct numbers at correct position
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
        if len(clues) == 0:
            return 'Bagels'
        else:
            # sort clues alphabetically not to help with orders
            clues.sort()
            return ' '.join(clues)

def main():
    print('''Bagels, a deductive logic game.
    You need to guess a {}-digit number.
    Here come clues:
    When I say:     That means:
        Pico        One digit is correct but in wrong position
        Fermi       One digit is correct and position is correct
        Bagels      No correct digits
    For example if secret number is 248, and your guess was 843, the clues will be Fermi Pico.'''.format(NUM_DIGITS))
    while True:
        secretNum = getSecretNum()  # Secret Number generation
        print("You should guess secret number that I'd though")
        print("You have {} attempts".format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}: '.format(numGuesses))
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break  # BINGO!
            if numGuesses > MAX_GUESSES:
                print('You run out of guesses.')
                print('The answer was: {}'.format(secretNum))

                    # Do you want to play again?
                print('Do you want to play again?')
            if not input('> ').lower().startswith('y'):
                break
        print('Thanks for game!')

if __name__ == '__main__':
    main()
