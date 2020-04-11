# 1) Create an empty set and assign it to a variable.
numbers = set()
print(numbers)


# 2) Add three items to your empty set using either several add calls, or a single call to update.
numbers.update(range(1, 6))
print(numbers)

# 3) Create a second set which includes at least one common element with the first set.
letters_and_numbers = {1, 'a', 2, 'b', 3, 'c'}

# 4) Find the union, symmetric difference, and intersection of the two sets. Print the results of each operation.
print(f"Union : {letters_and_numbers.union(numbers)}")
print(f"Intersection : {letters_and_numbers.intersection(numbers)}")
print(f"Symmetric difference : {letters_and_numbers.symmetric_difference(numbers)}")

""" 5) Create a sequence of numbers using range, then ask the user to enter a number. Inform the user whether or
not their number was within the range you specified and tell the user if their number was too high or too low."""
numbers = range(10, 100)
number = int(input("Enter a number "))
if number in numbers:
    print(f"{number} is within the range")
else:
    if number < numbers[0]:
        print(f"{number} is too low")
    else:
        print(f"{number} is too high")


