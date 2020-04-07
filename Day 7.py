"""1) Ask the user to enter their given name and surname in response to a single prompt. Use split to extract the names,
and then assign each name to a different variable. For this exercise, you can assume that the user has a single given
name and a single surname."""
name = input("Enter your name ( first and last name ) ").title().split(" ")
print(f"First name is {name[0]}")
print(f"Surname is {name[1]}")

"""2) Print the list, [1, 2, 3, 4, 5], in the format 1 | 2 | 3 | 4 | 5 using the join method. Remember that you can 
only join collections of strings, so you’re going to need to do some initial processing of the list of numbers."""
numbers = [1, 2, 3, 4, 5]
processed_numbers = []
for number in numbers:
    processed_numbers.append(str(number))
print(" | ".join(processed_numbers))

"""3) Below you’ll find a short list of quotes:
 quotes = [
    "'What a waste my life would be without all the beautiful mistakes I've made.'",
    "'A bend in the road is not the end of the road... Unless you fail to make the turn.'",
    "'The very essence of romance is uncertainty.'",
    "'We are not here to do what has already been done.'"
 ]
Each quote is a string, but each string actually contains quote characters at the start and end. Using slicing, 
extract the text from each string, without these extra quote marks, and print each quote.You may also want to 
try a solution using strip."""
quotes = [
    "'What a waste my life would be without all the beautiful mistakes I've made.'",
    "'A bend in the road is not the end of the road... Unless you fail to make the turn.'",
    "'The very essence of romance is uncertainty.'",
    "'We are not here to do what has already been done.'"
 ]
for quote in quotes:                # First Approach using slicing
    print(quote[1:-1])
for quote in quotes:                # Second Approach using strip function
    print(quote.strip("'"))


"""4) Ask the user to enter a word, and then print out the length of the word. You should account for any excess 
whitespace in the user’s input, so you’re going to have to process the string before you find its length.If you 
want to take this a little bit further, you an ask the user for a long piece of text. You can then tell them 
how many how many characters are in the text overall, and you can also provide them a word count."""
word = input("Enter a word ").strip()
print(f"Length of {word} entered is {len(word)}")
sentence = input("Enter the sentence ").strip()
print(f"Length of sentence is {len(sentence)}")
print(f"Number of words in sentence are {len(sentence.split(' '))}")
