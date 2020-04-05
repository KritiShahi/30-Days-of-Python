"""1) Try to approximate the behaviour of the is operator using ==. Remember we have the id function for
finding the memory address for a given value, and we can compare memory addresses to check for identity."""
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(id(list1) == id(list2))

list1 = [4, 5, 6]
list2 = list1
print(id(list1) == id(list2))

tuple1 = 1, 3
tuple2 = 1, 3
print(id(tuple1) == id(tuple2))

tuple1 = 4, 6
tuple2 = tuple1
print(id(tuple1) == id(tuple2))

"""2) Try to use the is operator or the id function to investigate the difference between this:
numbers = [1, 2, 3, 4]
new_numbers = numbers + [5]
And this:
numbers = [1, 2, 3, 4]
numbers.append(5)
Are new_numbers and numbers the same thing? What about numbers before and after we append 5?"""
numbers = [1, 2, 3, 4]
new_numbers = numbers + [5]
numbers = [1, 2, 3, 4]
numbers.append(5)
print(new_numbers is numbers)

# 3) Ask the user to enter a number. Tell the user whether the number is positive, negative, or zero.
num = float(input("Enter the number "))
if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")

"""4) Write a program to determine whether an employee is owed any overtime. You should ask the user how many hours 
the employee worked this week, as well as the hourly wage for this employee.If the employee worked more than 40 hours, 
you should print a message which says the employee is due some additional pay, as well as the amount due. 
The additional amount owed is 10% of the employees hourly wage for each hour worked over the 40 hours. In effect, 
the employees get paid 110% of their hourly wage for any overtime."""
hours_worked = float(input("Enter the number of hours worked this week "))
hourly_wage = float(input("Enter the hourly wage "))
if hours_worked > 40:
    print(f"Payment to the employee is ${(hourly_wage * 40 + 1.1 * hourly_wage * (hours_worked - 40)):.2f}")
else:
    print(f"Payment to the employee is ${(hours_worked * hourly_wage):.2f}")
