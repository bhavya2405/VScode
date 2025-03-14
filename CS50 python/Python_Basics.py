import math
print("Hello, World!")

print("3" * 10)


# STRINGS

course = "Python Programming"

len(course)
print(len(course))

print(course[:8])
print(course[:-2])
print(course[0])
print(course[1])
print(course[:])


course = "Python \" Programming"
print(course)

course = "Python \nProgramming"
print(course)


first = "Bhavya"
last = "Bhati"

full = first + " " + last
print(full)

full = f"{first} {last}"
print(full)

full = f"My name is {first} {last}"
print(full)


full = f"My name is {first} {last} its has {len(first) + len(last)} characters"
print(full)


# STRING METHODS


course = "   python programming"


print(course)
print(course.upper())
print(course.lower())
print(course.title())
print(course.lstrip())
print(course.rstrip())
print(course.find("pro"))
print(course.find("Pro"))
print(course.replace("p", "j"))
print("pro" in course)
print("swift" not in course)


######################
# NUMBERS
######################


print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)

x = 10
x = x + 3
x += 3
print(x)


######################
# MATH FUNCTIONS
######################


print(round(2.9))
print(abs(-2.9))

print(math.ceil(2.2))

"""
google "python 3 math module" practice with the functions 
"""


######################
# TYPE CONVERSION
######################

'''
x = input("x: ")
print(type(x))
y = int(x) + 1
print(f"x: {x}, y: {y}")
'''


# int(x)
# float(x)
# bool(x)
# str(x)


# Falsy values
# ""
# 0
# None

bool("False")
bool(" ")
bool("")


###################
# COMPARISON OPERATORS
###################

10 > 3
10 >= 3
10 < 20
10 <= 20
10 == 10
10 != 10
10 == "10"
"bag" > "apple"
"bag" > "cat"
"bag" == "BAG"  # they have different ASCII values


###################
# CONDITIONAL STATEMENT
###################

temperature = 15

if temperature > 30:
    print("It's warm")
    print("Drink water")
elif temperature > 20:
    print("It;s nice")
else:
    print("It's cold")
print("Done")


###################
# TERNARY OPERATORS
###################

age = 22

if age >= 18:
    message = "Eligible"
else:
    message = "Not Eligible"
print(message)

# Aleternative way(ternary operator)
age = 16
message = "Eligible" if age >= 18 else "Not Eligible"
print(message)

###################
# LOGICAL OPERATORS
###################

'''
and
or
not
'''

high_income = False
good_credit = True
student = True

if high_income and good_credit:  # "and" will give true when if both are true
    print("Eligible")
else:
    print("Not Eligible")


high_income = True
good_credit = True
student = True


if not student:  # "not" will give true when if value is false
    print("Eligible")
else:
    print("Not Eligible")


high_income = False
good_credit = True
student = False


if (high_income or good_credit) and not student:  # "or" will give true when if any one is true
    print("Eligible")
else:
    print("Not Eligible")


status = "Eligible for card" if (
    high_income or good_credit) and not student else "Not Eligible for card"
print(status)


###################
# SHORT-CIRCUIT EVALUATION
###################


high_income = False
good_credit = True
student = True


# when first condition is false it will not check the other conditions
if high_income and good_credit and not student:
    print("Eligible")

high_income = True
good_credit = False
student = False


# when first condition is true it will not check the other conditions
if high_income or good_credit or not student:
    print("Eligible")


###################
# CHAINING COMPARISON OPERATORS
###################

# age should be between 18 and 65
age = 22

# if age >= 18 and age < 65: # this is the long way
if 18 <= age < 65:  # this is the short way
    print("Eligible")


###################
# FOR LOOPS
###################

for number in range(3):
    print("Attempt", number + 1, (number + 1) * ".")

# or

for number in range(1, 4):
    print("Attempt", number, (number) * ".")


for number in range(1, 10, 2):  # 3rd argument is the step
    print("Attempt", number, (number) * ".")


###################
# FOR ELSE
###################

successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")


successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")


###################
# NESTED LOOPS  (for loop inside for loop)
###################


for x in range(5):  # outer loop
    for y in range(3):  # inner loop
        print(f"({x}, {y})")


###################
# ITERABLES (list, tuple, set, string)
###################

print(type(5))
print(type(range(5)))

# Iterable is an object that can be looped over

y = range(5)
for x in y:
    print(x)

y = "Python"
for x in y:
    print(x)

y = [1, 2, 3, 4, 5]
for x in y:
    print(x)

###################
# WHILE LOOPS
###################

# COMMENTING BECAUSE ASKING FOR INPUT IN TERMINAL
""" 
number = 100
while number > 0:
    print(number)
    number //= 2


command = ""
while command != "quit":
    command = input(">")
    print("ECHO", command)

# doesnt account for all edge cases and bad practice
command = ""
while command != "quit" and command != "QUIT":  # doesnt account for all edge cases and bad practice
    command = input(">")
    print("ECHO", command)

# better way
command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)


###################
# INFINITE LOOPS
###################


while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break

"""

#################
# FUNCTIONS
#################


def greet():
    print("Hi There")
    print("Welcome aboard")


greet()


#################
# ARGUMENTS
#################

def greet(first_name, last_name):
    print(f"Hi There {first_name} {last_name}!")
    print("Welcome aboard")


greet("Bhavya", "Bhati")
greet("Naki", "Baby")


#################
# TYPES OF FUNCTIONS
#################

# 1. Perform a task (function that does not return a value)

def greet(name):
    print(f"Hi {name}!")


greet("Bhavya")

# 2. Calculate and return a value (function that returns a value)


def get_greeting(name):  # better because we can save the value in a variable, has more flexibility
    return f"Hi {name}"


message = get_greeting("Bhavya")
print(message)


# Difference between 1 and 2

def greet(name):
    # print(f"Hi {name}!")
    return ("...")


print(greet("xyz"))


#################
# KEYWORD ARGUMENTS
#################

def increment(number, by):
    return number + by


# result = increment(2, 1)
# print(result)
print(increment(2, 1))  # or print(increment(2, by=1))


# making the by argument optional
def increment(number, by=1):
    return number + by


print(increment(2, 5))


#################
# XARGS
#################


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return (numbers, total)


print(multiply(2, 3, 4, 5))
