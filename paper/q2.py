class Book:
    def __init__(self, title, author, isbn, copies_available=1):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False
        self.copies_available = copies_available  # Set the number of copies available

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"The book '{self.title}' has been borrowed.")
        else:
            print(f"The book '{self.title}' is already borrowed.")

    def return_book(self):
        self.is_borrowed = False
        print(f"The book '{self.title}' has been returned.")

# Subclass: DigitalBook
class DigitalBook(Book):
    def __init__(self, title, author, isbn, file_format):
        super().__init__(title, author, isbn)
        self.file_format = file_format

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"The digital book '{self.title}' can be accessed online.")
        else:
            print(f"The digital book '{self.title}' is already borrowed.")

# Subclass: AudioBook
class AudioBook(Book):
    def __init__(self, title, author, isbn, duration):
        super().__init__(title, author, isbn)
        self.duration = duration

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"The AudioBook '{self.title}' can be borrowed.")
        else:
            print(f"The AudioBook '{self.title}' is not available.")

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.__borrowed_books = []

    def borrow_book(self, book):
        if not book.is_borrowed:
            book.borrow()
            self.__borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'.")
        else:
            print(f"Sorry, '{book.title}' is not available.")

    def return_book(self, book):
        if book in self.__borrowed_books:
            book.return_book()
            self.__borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'.")
        else:
            print(f"{self.name} can't be borrow '{book.title}'.")

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added '{book.title}' to the Library.")

    def register_user(self, user):
        self.users.append(user)
        print(f"Registered user '{user.name}' with ID: {user.user_id}.")

    def lend_book(self, user_id, isbn):
        user = next((i for i in self.users if i.user_id == user_id), None)
        book = next((a for a in self.books if a.isbn == isbn), None)

        if user and book:
            user.borrow_book(book)
        elif not user:
            print("User Not Found.")
        elif not book:
            print("Book Not Found.")

    def receive_return(self, user_id, isbn):
        user = next((i for i in self.users if i.user_id == user_id), None)
        book = next((a for a in self.books if a.isbn == isbn), None)

        if user and book:
            user.return_book(book)
        elif not user:
            print("User not found.")
        elif not book:
            print("Book not found.")

def main():
    library = Library("Quaid E Azam Library")
    book1 = Book("d.Engineering", "Sir Ayyan", "112233")
    book2 = DigitalBook("Python Programming", "Majid", "11111", "PDF")
    book3 = AudioBook("Java", "Sir Qasim", "1122", 23)

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    user1 = User("U1", "Hamza")
    user2 = User("U2", "Salim")

    library.register_user(user1)
    library.register_user(user2)

    library.lend_book("U1", "112233")  
    library.lend_book("U2", "11111")  

    library.receive_return("U1", "112233")  
    library.lend_book("U2", "1122")  

if __name__ == "__main__":
    main()
