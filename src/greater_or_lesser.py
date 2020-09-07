import random
import time
import sys


def guessing_game():
    print("Do you want to play a guessing game? y/n")
    should_play = input()
    if should_play.lower() == 'y':
        print("Think of a number between 1 and 100.")
        time.sleep(2)
        print("Do you have it?")
        time.sleep(.5)
        highest = 101
        lowest = 1
        guess = random.randrange(lowest, highest)
        print(f"Okay! My guess is {guess}! Am I right? y/n")
        correct = input()
        while correct.lower() not in ['y', 'n']:
            print(f"You have to tell me if I got it! Was {guess} correct? y/n")
            correct = input()
        while correct.lower() == 'n':
            guess, lowest, highest = that_wasnt_right(guess, lowest, highest)
            print(f"Okay! My new guess is {guess}! Am I right? y/n")
            correct = input()
            while correct.lower() not in ['y', 'n']:
                print(f"You have to tell me if I got it! Was {guess} correct? y/n")
        if correct.lower() == 'y':
            print("Hooray!")
            sys.exit()


def that_wasnt_right(guess, lowest, highest):
    print(f"If your number is higher than {guess}, enter 'higher'. If it's lower than {guess}, enter 'lower'. ")
    h_or_l = input()
    while h_or_l.lower() not in ['higher', 'lower']:
        print("That's not right!")
        print(f"If your number is higher than {guess}, enter 'higher'. If it's lower than {guess},"
              f" enter 'lower'. ")
    if h_or_l.lower() == 'higher':
        new_guess = random.randrange(guess, 101)
        lowest = guess
    else:
        new_guess = random.randrange(0, guess)
        highest = guess
    return new_guess, lowest, highest


if __name__ == "__main__":
    guessing_game()
