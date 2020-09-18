# a guessing number game
import random
def guess_the_number():
    GuessesTaken = 0

    print('Hello! What is your name?')
    UserName = input()

    number = random.randint(1, 20)
    print('Well ' + UserName + ', I am thinking of a number between 1 and 20.')

    for GuessesTaken in range(6):
        print('Take a guess')
        guess = input()
        guess = int(guess)
        
        if guess < number:
            print('your guess is too low!')

        if guess > number:
            print('your guess is too high')

        if guess == number:
            break

    if guess == number:
        GuessesTaken = str(GuessesTaken + 1)
        print('Good job,' + UserName + '! You Guessed my number in ' + GuessesTaken + ' guesses!')
    else: 
        print('nope. the number i was thinking of was ' + str(number) + '.')

guess_the_number()