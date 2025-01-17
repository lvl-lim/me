# -*- coding: UTF-8 -*-
"""Set 3.

Modify each function until the tests pass.
"""


from re import T


def loop_ranger(start, stop=None, step=1):
    """Return a list of numbers between start and stop in steps of step.

    Do this using any method apart from JUST using range() #TODO: clarify this wording
    The look up the docs for range(), you can answer this with just the range
    function, but we'd like you to do it the long way, probably using a loop.
    """

    bucket = []
    while start < stop:
        bucket.append(start)
        start += step
    return bucket


def lone_ranger(start, stop, step):
    """Duplicate the functionality of range.

    Look up the docs for range() and wrap it in a 1:1 way
    """
    return list(range(start, stop, step))


def two_step_ranger(start, stop):
    """Make a range that steps by 2.

    Sometimes you want to hide complexity.
    Make a range function that always has a step size of 2

    You can either reuse loop_ranger, or the range function that in the standard library
    """

    return list(range(start, stop, 2))


def stubborn_asker(low, high):
    """Ask for a number between low and high until actually given one.

    Ask for a number, and if the response is outside the bounds keep asking
    until you get a number that you think is OK

    Look up the docs for a function called "input"
    """

    while True:
        try:
            the_input = input(f"give me a number between {low} and {high}: ")
            answer = int(the_input)

            if low < answer < high:
                print("❤😍👌👌💖👏👏👏")
                return answer
            else:
                print("that number is outside the bounds")
        except:
            print("that's not a number, dodo!")


def not_number_rejector(message):
    """Ask for a number repeatedly until actually given one.

    Ask for a number, and if the response is actually NOT a number
    (e.g. "cow", "six", "8!") then throw it out and ask for an actual number.
    When you do get a number, return it.
    """
    while True:
        try:
            the_input = input(f"give me a number: ")
            answer = int(the_input)

            if answer > 0:
                return answer
            else:
                print("that's not a number")
        except:
            print("try again please")


def super_asker(low, high):
    """Robust asking function.

    Combine what you learnt from stubborn_asker and not_number_rejector
    to make a function that does it all!
    """
    while True:
        try:
            the_input = input(f"give me a number between {low} and {high}: ")
            answer = int(the_input)

            if low < answer < high:
                print("❤😍👌👌💖👏👏👏")
                return answer
            else:
                print("that number is outside the bounds")
        except:
            print("that's not a number, dodo!")


if __name__ == "__main__":
    # this section does a quick test on your results and prints them nicely.
    # It's NOT the official tests, they are in tests.py as usual.
    # Add to these tests, give them arguments etc. to make sure that your
    # code is robust to the situations that you'll see in action.
    # NOTE: because some of these take user input you can't run them from

    print("\nloop_ranger", loop_ranger(1, 10, 2))
    print("\ntwo_step_ranger", two_step_ranger(1, 10))
    print("\nstubborn_asker")
    stubborn_asker(30, 45)
    print("\nnot_number_rejector")
    not_number_rejector("Enter a number: ")
    print("\nsuper_asker")
    super_asker(33, 42)
