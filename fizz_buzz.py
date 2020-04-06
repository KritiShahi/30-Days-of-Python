"""The computer is going to play the first 100 rounds of Fizz Buzz all by itself. In other words, we need to
print out the first 100 items in the sequence, starting from 1. If the number is divisible by 3, the player
should say, "Fizz".If the number is divisible by 5, the player should say, "Buzz".If the number is divisible by 3 and 5,
the player should say, "Fizz Buzz"""
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("Fizz Buzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
