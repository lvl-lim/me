TODO: Reflect on what you learned this week and what is still unclear.

checking if user input is an integer:

can we do...
if (user input) \* 0 != 0?
if user input != int(user input)
these did not work when i tried them... the code would crash

can we program a different response for the first 3 attempts?

print("\nWelcome to the guessing game!")
while True:
lowerBound = input("Enter a lower bound: ")

        if lowerBound.isdigit():
            break
        else:
            print("Not a valid answer. Please try again.")

    while True:
        upperBound = input("Enter a upper bound: ")

        if upperBound.isdigit():
            break
        else:
            print("Not a valid answer. Please try again.")
