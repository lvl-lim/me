"""Set 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    You can refactor a bit, you should refactor a bit! Don't put the code all
    inside this function, think about reusable chunks of code that you can call
    in several places.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """

    print("\nWelcome to the guessing game!")
    while True:
        try:
            lowerBound = input("Enter a lower bound: ")
            lowerBoundcheck = int(lowerBound)
            break
        except:
            print("Not a valid answer. Please try again.")

    while True:
        try:
            upperBound = input("Enter a upper bound: ")
            upperBoundcheck = int(upperBound)
            break
        except:
            print("Not a valid answer. Please try again.")

    print(f"Alrighty then, a number between {lowerBound} and {upperBound} ?")

    lowerBound = int(lowerBound)
    upperBound = int(upperBound)

    actualNumber = random.randint(lowerBound, upperBound)

    guessed = False
    counter = 0

    while not guessed:
        try:
            guessedNumber = int(input("Guess a number: "))
            print(f"You guessed {guessedNumber},")
            if guessedNumber == actualNumber:
                print("Hooray!".format(actualNumber))
                guessed = True
            if guessedNumber > upperBound or guessedNumber < lowerBound:
                print("... Time to go back to pre-school!")
                counter += 1
                if counter > 2:
                    print("Do you even math?")
            elif guessedNumber < actualNumber:
                print("Too small, try again :'(")
            elif guessedNumber > actualNumber:
                print("Too big, try again :'(")
        except:
            print("That's not a number, dodo!")
    return "You got it!"
    # the tests are looking for the exact string "You got it!". Don't modify that!


if __name__ == "__main__":
    print(advancedGuessingGame())
