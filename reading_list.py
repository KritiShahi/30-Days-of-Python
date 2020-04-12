"""For this project the application needs to have the following functionality:
Users should be able to add a book to their reading list by providing a book title, an author's name,
and a year of publication.The program should store information about all of these books in a Python list.
Users should be able to display all the books in their reading list, and these books should be printed out
in a user-friendly format.Users should be able to select these options from a text menu, and they should be
able to perform multiple operations without restarting the program."""


def add_book():
    book_name = input("Enter the book name ").title().strip()
    author_name = input("Enter the author name ").title().strip()
    year = input("Enter the year of publication ").title().strip()

    reading_list.append({
        "book_name": book_name,
        "author_name": author_name,
        "year":  year
    })
    return reading_list


def print_book():
    for book in reading_list:
        print(f"{book['book_name']} by {book['author_name']} released in {book['year']}")


reading_list = []
menu_prompt = "Enter 'a' for adding the book, 'p' for printing the reading list and 'q' for quit "
while True:
    selected_option = input(menu_prompt).strip().lower()
    if selected_option == 'q':
        break
    elif selected_option == 'a':
        add_book()
    elif selected_option == 'p':
        if reading_list:
            print_book()
        else:
            print("Reading list is empty")
    else:
        print("Not a valid option")
