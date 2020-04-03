"""1. Using the variable below, print "Hello, world!".
greeting = "Hello, world"
You can add the missing exclamation mark using string concatenation, format, or f-strings. The choice is yours."""
greeting = "Hello, world"
print(greeting + "!")                       # Using string concatenation
print("{}{}".format(greeting, "!"))         # Using format
print(f"{greeting}!")

"""2. Ask the user for their name, and then greet the user, using their name as part of the greeting. 
The name should be in title case, and shouldn't be surrounded by any excess white space.
For example, if the user enters "lewis ", your output should be something like this: Hello, Lewis!"""
name = input("Enter your name")
print(f"Hello, {name.title().strip()}!")

"""3. Concatenate the string "I am " and the integer 29 to produce a string which reads "I am 29".
Remember that we can only concatenate strings to other strings, so you will have to convert the integer to a string 
before you can perform the concatenation."""
age = str(29)
print("I am "+age)

"""4. Format and print the information below using string interpolation:
title = "Joker"
director = "Todd Phillips"
release_year = 2019
The output should look like this:
Joker (2019), directed by Todd Phillips"""
title = "Joker"
director = "Todd Phillips"
release_year = 2019
print(f"{title}({str(release_year)}), directed by {director}")