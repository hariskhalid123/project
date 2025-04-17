import json

# Initialize the book list with some default data
book_list = ["The jungle book", "the evil died", "1984"]

menu = """
1) ADD BOOK
2) REMOVE BOOK
3) VIEW BOOK
4) PRESS E TO EXIT
"""

def add_book(book_list, book):
    book_list.append(book)
    print("Book added successfully.\n")

def remove_book(book_list, book):
    if book in book_list:
        book_list.remove(book)
        print("Book removed successfully.\n")
    else:
        print("Book not found in the list.\n")

def view_book():
    if book_list:
        print("Books in list -> " + ", ".join(book_list) + "\n")
    else:
        print("No book in the list.\n")

def exit_program():
    print("Thank you for visiting!")
    quit()

while True:
    print(menu)
    choice = input("Your choice: ")

    if choice == '1': 
        book = input("Enter the book name: ")
        add_book(book_list, book)
    elif choice == '2':
        book = input("Enter the book name to remove: ")
        remove_book(book_list, book)
    elif choice == '3':
        view_book()
    elif choice.lower() == 'e' or choice == '4':
        exit_program()
    else:
        print("Invalid entry.\n")
        input("Press enter to return to the main menu!")