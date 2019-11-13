# This is a guess a number game.

import random

print("Hello! What is your name?")
userName = input()
print("Nice to meet you, " + userName+ ". Let's play a guess a number game, shall we?")


while True:
    secretNumber = random.randint(1, 20)
    print("I am thinking of a number between 1 and 20")

    # Ask the player to guess 5 times

    for guessTaken in range(1, 6):
        print("Take a guess:")
        try:
            guess = int(input())
            if guess > secretNumber:
                print("Your guess is too high!")
            elif guess < secretNumber:
                print("You guess is too low!")
            else:
                break # Stop the loop if guess correctly
        except ValueError:
            print("Invalid input. Please try again!")

    if guess == secretNumber:
        print("Congratulation, " + userName + ". You guess correctly in " + str(guessTaken) + " times!")
    else:
        print("Out of guess. The number I was thinking of was " + str(secretNumber))

    print("Do you want to continue? Press Y to continue or any other keys to exit!")
    userContinue = input()
    if userContinue == "Y" or userContinue == "y":
        continue
    else:
        break
quit()
