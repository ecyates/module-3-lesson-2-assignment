# 2 Library System Enhancement
# Problem Statement: You are maintaining a library system where each book is stored as a tuple within a list. 
# Your task is to update this system by adding new books and ensuring no duplicates.

# Add functionality to insert new books into `library`. 
# Ensure that adding a duplicate book is handled appropriately.

# Existing Library Data:
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def add_books(*books):
    '''This function takes a list of tuples (book, author) and adds them to the library.'''
    try:
        # Iterate through the books in the list
        for book in books:
            # Check that the input is valid
            if isinstance(book, tuple) and len(book)==2:
                # Check that the book is not a duplicate
                found = [library_book for library_book in library if library_book[0].lower() == book[0].lower()]
                if found:
                #if book in library:
                    print(f"The book entitled '{book[0]}' by {book[1]} is already in the library.")
                else: 
                    # Add it to the library and alert user
                    library.append(book)
                    print(f"The book {book[0]} by {book[1]} has been added to the library.")
            else:
                raise ValueError()
    except ValueError:
        print("This is not a valid book input. Try again!")

# Adding one book
add_books(("Harry Potter: The Sorcerer's Stone", "JK Rowling"))
print(library)
# Adding multiple books
add_books(("The Idiot", "Fyodor Dostoevsky"), ("I, Robot", "Isaac Asimov"), ("The Hobbit", "JRR Tolkien"))
print(library)
# Testing various errors: invalid input, too many indices, duplicate entry
add_books("Testing")
add_books(("Book123", "Author123","Too Many Indices"))
add_books(("The Idiot", "Fyodor Dostoevsky"))
print(library)