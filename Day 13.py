"""1) Define a exponentiate function that takes in two numbers. The first is the base, and the second is the power
to raise the base to. The function should return the result of this operation"""


def exponentiate(base, exponent):
    return int(base) ** int(exponent)


base, exponent = input("Enter two numbers ").split()
print(f"Result of exponentiation operation is {exponentiate(base, exponent)}")

"""2) Define a process_string function which takes in a string and returns a new string which has been converted to 
lowercase, and has had any excess whitespace removed."""


def process_string(s):
    return s.lower().strip()


s = input("Enter a sentence ")
print(process_string(s))

""""3) Write a function that takes in a tuple containing information about an actor and returns this data as a 
dictionary. The data should be in the following format: ("Tom Hardy", "English", 42)  - name, nationality, age"""


def show_info(actor_data):
    name, nationality, age = actor_data
    return {
        "name": name,
        "nationality": nationality,
        "age": age
    }


name = input("Enter the name ")
nationality = input("Enter the nationality ")
age = input("Enter the age ")
print(show_info((name, nationality, age)))

# 4) Write a function that takes single number and returns True or False depending on whether or not the number is prime


def check_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


num = int(input("Enter a number "))
res = check_prime(num)
if res == True:
    print(f"{num} is a prime number ")
else:
    print(f"{num} is not a prime number ")
