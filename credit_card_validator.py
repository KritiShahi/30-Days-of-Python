"""1) It should be able to accept a card number from the user. For this project, you can assume that
the number will be entered as a single string of characters (i.e. there won't be any spaces between the numbers).
However, you should be able to accept a card number with spaces at the start or end of the string.If you
want to challenge yourself, you should try to be more versatile with regards to the format that you accept card
numbers in.You may want to turn the user's input into a list of numbers, as that will make it easier to work with."""
"""2) The program should validate that card number using the Luhn algorithm described. After removing the checking 
digit and reversing the card number, you'll need a for loop to go over the credit card numbers. As you go through 
each digit, you must find a way to determine whether a digit is in an odd or an even position."""
"""3) Once the validation is complete, the program should inform the user whether or not the card number is valid 
by printing a string to the console.When you need to get to the step where you reverse the numbers you could 
use the reversed function, which will accept any sequence type:
language = "Python"
numbers = [1, 2, 3, 4, 5]
letters = ("a", "b", "c", "d", "e")
language = reversed(language)    # 'nohtyP'
numbers = reversed(numbers)      # [5, 4, 3, 2, 1]
letters = reversed(letters)      # ('e', 'd', 'c', 'b', 'a')
reversed will give us back a lazy type (like range), so we can't directly print it; however, it is iterable. 
We can therefore use the result in a for loop, for example.If our numbers are in a list, we can use the 
reverse method. This directly modifies the original list:
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)  # [5, 4, 3, 2, 1]
You can use whichever technique you prefer.
When testing your solution, you can use your own card number, or you can find valid card numbers online that are 
used for testing payment methods. For example, Stripe has a range of test card numbers you can use."""
card_num = list(input("Enter a credit card number").strip())
check_digit = int(card_num.pop())
card_num.reverse()
total = 0
for index, num in enumerate(card_num):
    if (index % 2) == 0:
        num = int(num) * 2
        if num > 9:
            num = num - 9
    total += int(num)

if (total+check_digit) % 10 == 0:
    print("Valid Card Number")
else:
    print("Invalid Card Number")
