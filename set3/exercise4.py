# -*- coding: UTF-8 -*-
"""Set 3, Exercise 4."""


from decimal import ROUND_UP
import math

# import time


def binary_search(low, high, actual_number):
    """Do a binary search.

    This is going to be your first 'algorithm' in the usual sense of the word!
    you'll give it a range to guess inside, and then use binary search to home
    in on the actual_number.

    Each guess, print what the guess is. Then when you find the number return
    the number of guesses it took to get there and the actual number
    as a dictionary. make sure that it has exactly these keys:
    {"guess": guess, "tries": tries}

    This will be quite hard, especially hard if you don't have a good diagram!

    Use the VS Code debugging tools a lot here. It'll make understanding
    things much easier.
    """
    tries = 0
    guess = 0

    while high >= low:
        mid = round((high + low) / 2)
        if actual_number == mid:
            tries += 1
            return {"guess": mid, "tries": tries}
        if actual_number == high:
            tries += 1
            return {"guess": high, "tries": tries}
        if actual_number == low:
            tries += 1
            return {"guess": low, "tries": tries}
        if actual_number == mid:
            tries += 1
            return {"guess": mid, "tries": tries}
        elif actual_number > mid:
            low = mid + 1
            tries += 1
            print({"guess": mid, "tries": tries})
        elif actual_number < mid:
            high = mid - 1
            tries += 1
            print({"guess": mid, "tries": tries})
        else:
            print("what's going on")


if __name__ == "__main__":
    print(binary_search(1, 100, 5))
    print(binary_search(1, 100, 6))
    print(binary_search(1, 100, 95))
    print(binary_search(1, 51, 5))
    print(binary_search(1, 50, 5))
