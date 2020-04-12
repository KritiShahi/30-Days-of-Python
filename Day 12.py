"""1) Define four functions: add, subtract, divide, and multiply. Each function should take two arguments, and
they should print the result of the arithmetic operation indicated by the function name.When orders matters for
an operation, the first argument should be treated as the left operand, and the second argument should be treated
as the right operand. For example, if the user passes in 6 and 2 to subtract, the result should be 4, not -4.
You should also make sure that the user can’t pass in 0 as the second argument for divide. If the user provides 0,
you should print a warning instead of calculating their division."""


def add(num1, num2):
    print(f"Result of addition is {num1 + num2}")


def subtract(num1, num2):
    print(f"Result after subtraction is {num1 - num2}")


def multiply(num1, num2):
    print(f"Result after multiplication is {num1 * num2}")


def divide(num1, num2):
    if num2 == 0:
        print("Division is not possible")
    else:
        print(f"Result after division is {num1 / num2}")


add(5, 10)
subtract(5, 6)
multiply(8, 1)
divide(6, 0)

"""2) Define a function called print_show_info that has a single parameter. The argument passed to it will be 
a dictionary with some information about a T.V. show. For example:
tv_show = {
    "title": "Breaking Bad",
    "seasons": 5,
    "initial_release": 2008
 }
print_show_info(tv_show)
The print_show_info function should print the information stored in the dictionary, in a nice way. For example:
Breaking Bad (2008) - 5 seasons
Remember you must define your function before calling it!"""


def print_show_info(tv_show):
    print(f"{tv_show['title']} ({tv_show['initial_release']}) - {tv_show['seasons']} seasons")


tv_show = {
    "title": "Breaking Bad",
    "seasons": 5,
    "initial_release": 2008
 }
print_show_info(tv_show)

"""3) Below you’ll find a list containing details about multiple TV series.
 series = [
    {"title": "Breaking Bad", "seasons": 5, "initial_release": 2008},
    {"title": "Fargo", "seasons": 4, "initial_release": 2014},
    {"title": "Firefly", "seasons": 1, "initial_release": 2002},
    {"title": "Rick and Morty", "seasons": 4, "initial_release": 2013},
    {"title": "True Detective", "seasons": 3, "initial_release": 2014},
    {"title": "Westworld", "seasons": 3, "initial_release": 2016},
 ]
Use your function, print_show_info, and iterate over the series list, and call your function once for each 
iteration, passing in each dictionary. You should end up with each series printed in appropriate format."""


def print_show_info(tv_show):
    print(f"{tv_show['title']} ({tv_show['initial_release']}) - {tv_show['seasons']} seasons")


series = [
    {"title": "Breaking Bad", "seasons": 5, "initial_release": 2008},
    {"title": "Fargo", "seasons": 4, "initial_release": 2014},
    {"title": "Firefly", "seasons": 1, "initial_release": 2002},
    {"title": "Rick and Morty", "seasons": 4, "initial_release": 2013},
    {"title": "True Detective", "seasons": 3, "initial_release": 2014},
    {"title": "Westworld", "seasons": 3, "initial_release": 2016},
 ]
for serial in series:
    print_show_info(serial)

"""4) Create a function to test if a word is a palindrome. A palindrome is a string of characters that are identical 
whether read forwards or backwards. """


def check_palindrome(word):
    word = list(word.strip().lower())
    if word == list(reversed(word)):
        print("Palindrome")
    else:
        print("Not a Palindrome")


word = input("Enter a word")
check_palindrome(word)

