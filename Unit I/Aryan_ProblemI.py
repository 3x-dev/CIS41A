'''
Aryan Singhal
CIS 41A   Winter 2024
Unit I, Problem I
'''

class LibraryPatron:
    def __init__(self, name):
        self.name = name
        self.booksCheckedOut = []

    def checkOutBook(self, checkOutLimit, bookTitle):
        if len(self.booksCheckedOut) >= checkOutLimit:
            print(f"Sorry {self.name} you are at your limit of {checkOutLimit} books")
        else:
            self.booksCheckedOut.append(bookTitle)
            print(f"{self.name} has checked out {bookTitle}")

    def returnBook(self, book):
        bookTitle = book[0]
        if bookTitle in self.booksCheckedOut:
            self.booksCheckedOut.remove(bookTitle)
            print(f"{self.name} has returned {bookTitle}")

    def printCheckedOutBooks(self):
        print(f"{self.name} has the following books checked out:")
        for book in self.booksCheckedOut:
            print(book)

class AdultPatron(LibraryPatron):
    def __init__(self, name):
        super().__init__(name)
        self.checkOutLimit = 4

    def checkOutBook(self, book):
        bookTitle, bookType = book
        super().checkOutBook(self.checkOutLimit, bookTitle)

class JuvenilePatron(LibraryPatron):
    def __init__(self, name):
        super().__init__(name)
        self.checkOutLimit = 2

    def checkOutBook(self, book):
        bookTitle, bookType = book
        if bookType != "Juvenile":
            print(f"Sorry {self.name} {bookTitle} is an adult book")
        else:
            super().checkOutBook(self.checkOutLimit, bookTitle)

# Testing
book1 = ["Alice in Wonderland", "Juvenile"]
book2 = ["The Cat in the Hat", "Juvenile"]
book3 = ["Harry Potter and the Sorcerer's Stone", "Juvenile"]
book4 = ["The Hobbit", "Juvenile"]
book5 = ["The Da Vinci Code", "Adult"]
book6 = ["The Girl with the Dragon Tattoo", "Adult"]

patron1 = JuvenilePatron("Jimmy")
patron2 = AdultPatron("Sophia")

patron1.checkOutBook(book6)
patron1.checkOutBook(book1)
patron1.checkOutBook(book2)
patron1.printCheckedOutBooks()
patron1.checkOutBook(book3)
patron1.returnBook(book1)
patron1.checkOutBook(book3)
patron1.printCheckedOutBooks()
patron2.checkOutBook(book5)
patron2.checkOutBook(book4)
patron2.printCheckedOutBooks()


'''
Execution results:
Sorry Jimmy The Girl with the Dragon Tattoo is an adult book
Jimmy has checked out Alice in Wonderland
Jimmy has checked out The Cat in the Hat
Jimmy has the following books checked out:
Alice in Wonderland
The Cat in the Hat
Sorry Jimmy you are at your limit of 2 books
Jimmy has returned Alice in Wonderland
Jimmy has checked out Harry Potter and the Sorcerer's Stone
Jimmy has the following books checked out:
The Cat in the Hat
Harry Potter and the Sorcerer's Stone
Sophia has checked out The Da Vinci Code
Sophia has checked out The Hobbit
Sophia has the following books checked out:
The Da Vinci Code
The Hobbit
'''