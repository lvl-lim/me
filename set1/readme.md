TODO: Reflect on what you learned this week and what is still unclear.
hello

Self Exercises on Youtube

--VARIABLES, INPUT & TYPE CONVERSION--

Exercise 1
We check in a patient named John Smith.
He is 20 years old.
He is a new patient.

first_name = "John"
last_name = "Smith"
age = 20
existing_patient = False

print("Name: " + first_name + " " + last_name)
print("Age: " + str(age))
if existing_patient == True:
print("New Patient: " + "No")
if existing_patient == False:
print("New Patient: " + "Yes")

name = input("What is your name? ")
print("Hello " + name + "!")

birth_year = input("What is your birth year? ")
age = 2022 - int(birth_year)
print(age)

CONVERSION FUNCTIONS:
int()
float()
bool()
str()

Simple Calculator

First = float(input("First Number: "))
Second = float(input("Second Number: "))
Sum = First + Second
print("Sum: " + str(Sum))

STRINGS & METHODS

course = "Python for Beginners"
print(course.upper())
print(course)

course = "Python for Beginners"
print(course.find("y"))

course = "Python for Beginners"
print(course.replace("for", "4"))

course = "Python for Beginners"
print("Python" in course)

#this returns a boolean True or False

--ARITHMETIC OPERATORS--
print(10 + 3) typical addition, subtraction, multiplication
print(10 / 3) normal division - returns floating number with decimal
print(10 // 3) returns integer - whole number
print(10 % 3) modulus operator - returns remainder of division
print(10 \*\* 3) exponent operator - in this case, 10 to the power of 3

x = 10
x = x + 3
Augmented assignment operator
"x += 3"
"x -= 3"
"x \*= 3"

--COMPARISON OPERATOR--
x = 3 > 2 returns a boolean True or False
">" MORE THAN
">=" MORE THAN OR EQUAL TO
"<" LESS THAN
"<=" LESS THAN OR EQUAL TO
"==" EQUAL TO
"!=" NOT EQUAL TO

--LOGICAL OPERATOR--

and (both)
or (at least one)
not (inverses value)

print = 25
print(price > 10) returns TRUE

print(price > 10 and prince <30) both statements must be true
print(price > 10 or prince <30) only one statements needs to be true to return true

--IF STATEMENTS--

temperature = 25

if temperature > 30:
print("It's a hot day!")
print("Drink plenty of water")
elif temperature > 20: # (20 , 30)
print("Perfect Weather! Picnic Time!")
elif temperature > 10: # (10 , 20)
print("It's a bit cold today... Wrap up!")
else:
print("I'm freezing my butt off!")
print("Done")

--EXERCISE--
Create a weight convertor program that converts lbs to kg

Weight = int(input("What is your weight? "))
Unit = input("(K)g or (L)bs): ")
Weight_in_lbs = int((Weight) \* 2.205)
Weight_in_kg = int((Weight) / 2.205)

if Unit == "K" or Unit == "k":
print("Converted Weight: " + str(Weight_in_lbs) + " lbs")
elif Unit == "L" or Unit == "l":
print("Converted Weight: " + str(Weight_in_kg) + " kg")
else:
print("Not a valid input. Try again please.")
