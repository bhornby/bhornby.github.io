# a dice rolling game
import random

print ('Welcome to the Hornby cassino where HUGE winnings can be made!')

print ('what is your name')
name = input ()

print ('thank you, now follow me...')

print ('*You have now arrived at the DICE table*')

number = random.randint(1,6)
guessTaken = 0

for guessTaken in range(2):
    print ('Guess which number will be rolled. you have TWO guesses!')
    guess =  input()
    try:
        guess = int(guess)
        if guess > number :
            print ('just a little lower')
        elif guess < number :
            print ('just a little higher')
    except Exception:
        print('please enter a valid number')


if guess == number:
    print ("well done you've taken our money")
else: 
    print ('you are now my slave mwuhahahaha')