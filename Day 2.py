# 1. Ask the user for their name and age, assign theses values to two variables, and then print them.
name = input("Enter your name")
age = input("Enter your age")
print("Name of user is ", name, " and age is ", age)

"""2. Investigate what happens when you try to assign a value to a variable that you’ve already defined.
Try printing the variable before and after you reuse the name"""
name = "Aditya"
print("Changed name of user is ", name)

"""3. Below you’ll find some code with a number of errors. Try to go through the program line by line and 
fix the issues in the code. I’d encourage you to try running the program while you’re working on it, 
as reading the error messages is great practice for debugging your own programs
hourly_wage = input("Please enter your hourly wage: ')
prnt("Hourly wage: ")
print(hourlywage)
print("Hours worked: ")
print(hours_worked)
hours_worked = input("How many hours did you work this week? ")"""
hourly_wage = input("Please enter your hourly wage: ")
hours_worked = input("Please enter the hours worked ")
print("Hourly wage: ")
print(hourly_wage)
print("Hours worked: ")
print(hours_worked)

