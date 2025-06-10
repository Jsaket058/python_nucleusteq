# 9. Design a class structure for a library system with books and members.

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def __str__(self):
        status = "Available" if self.is_available else "Checked out"
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn}) - {status}"


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.is_available:
            self.borrowed_books.append(book)
            book.is_available = False
            print(f"{self.name} borrowed {book.title}.")
        else:
            print(f"Sorry, '{book.title}' is not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.is_available = True
            print(f"{self.name} returned {book.title}.")
        else:
            print(f"{self.name} did not borrow {book.title}.")

    def __str__(self):
        return f"Member: {self.name} (ID: {self.member_id})"


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added book: {book.title}")

    def add_member(self, member):
        self.members.append(member)
        print(f"Added member: {member.name}")

    def find_book_by_title(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def show_books(self):
        print("Library Books:")
        for book in self.books:
            print(f"  - {book}")

    def show_members(self):
        print("Library Members:")
        for member in self.members:
            print(f"  - {member}")

# Create library
library = Library()

# Add books
book1 = Book("1984", "George Orwell", "1234567890")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "0987654321")
library.add_book(book1)
library.add_book(book2)

# Add members
member1 = Member("Saket", 1)
member2 = Member("Vaseem", 2)
library.add_member(member1)
library.add_member(member2)

# Borrow and return books
member1.borrow_book(book1)  
member2.borrow_book(book1)  
member1.return_book(book1)  
member2.borrow_book(book1)  

# Show current status
library.show_books()
library.show_members()
