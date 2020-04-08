"""1) Write a short guessing game program using a while loop. The user should be prompted to guess a number
 between 1 and 100, and you should tell them whether their guess was too high or too low after each guess.
 The loop should keeping running until the user guesses the number correctly."""
from random import randint
guess_num = int(input("Enter the number between 1 and 100 "))
target_num = randint(1, 100)
print(f"Target number is {target_num}")
while guess_num != target_num:
    if guess_num < target_num:
        print("Guess is too low")
    elif guess_num > target_num:
        print("Guess is too high")
    guess_num = int(input("Enter the number between 1 and 100 "))
print("Guess is correct")

# 2) Use a loop and the continue keyword to print out every character in the string "Python", except the "o".
word = "Python"
for char in word:
    if char == 'o':
        continue
    print(char)

# 3) Create a program that prints out every prime number between 1 and 100.
primes = []
for num in range(2, 101):
    for val in range(2, num):
        if (num % val) == 0:
            break
    else:
        primes.append(str(num))
print(", ".join(primes))

