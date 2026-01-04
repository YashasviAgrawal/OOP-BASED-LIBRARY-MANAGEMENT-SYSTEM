import json

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = False
    def display(self):
        print(self.book_id, self.title, self.author)
    def to_dict(self):
        return {
            "type": "Book",
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "is_borrowed": self.is_borrowed
        }


class EBook(Book):
    def __init__(self, book_id, title, author, file_size):
        super().__init__(book_id, title, author)
        self.file_size = file_size
    def display(self):
        print(self.book_id, self.title, self.author, f"File Size: {self.file_size}")
    def to_dict(self):
        data = super().to_dict()
        data["type"] = "EBook"
        data["file_size"] = self.file_size
        return data


class PrintedBook(Book):
    def __init__(self, book_id, title, author, pages):
        super().__init__(book_id, title, author)
        self.pages = pages
    def display(self):
        print(self.book_id, self.title, self.author, f"Pages: {self.pages}")
    def to_dict(self):
        data = super().to_dict()
        data["type"] = "PrintedBook"
        data["pages"] = self.pages
        return data

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = []

class Library:
    def __init__(self):
        self.books = []
        self.users = []
    
    def save_data(self):
        data = {
            "books": [b.to_dict() for b in self.books],
            "users": [
                {
                    "user_id": u.user_id,
                    "name": u.name,
                    "borrowed_books": u.borrowed_books
                }
                for u in self.users
            ]
        }

        with open("library.json", "w") as file:
            json.dump(data, file, indent=4)

        print("Data saved successfully")
    

    def load_data(self):
        try:
            with open("library.json", "r") as file:
                data = json.load(file)

            self.books = []
            for b in data["books"]:
                if b["type"] == "PrintedBook":
                    book = PrintedBook(
                        b["book_id"], b["title"], b["author"], b["pages"]
                    )
                elif b["type"] == "EBook":
                    book = EBook(
                        b["book_id"], b["title"], b["author"], b["file_size"]
                    )
                else:
                    book = Book(
                        b["book_id"], b["title"], b["author"]
                    )

                book.is_borrowed = b["is_borrowed"]
                self.books.append(book)

            self.users = []
            for u in data["users"]:
                user = User(u["user_id"], u["name"])
                user.borrowed_books = u["borrowed_books"]
                self.users.append(user)

            print(" Data loaded successfully")

        except FileNotFoundError:
            print(" No previous data found")


    def view_books (self):
        for b in self.books:
            b.display()
    
    def userview (self):
        for u in self.users:
            print (u.user_id, u.name)

    def create_book(self):
        
        book_id = int (input (" enter the book_id "))
        book_name = (input ("enter the book name "))
        author_name = input ("enter the author name")

        type = input ("which kind of book \n 1. printed\n 2. ebook")


        if type == "1":
            pages_no = input ("enter the total number of pages: ")
            book = PrintedBook (book_id, book_name, author_name,  pages_no)
        
        elif type == "2":
            file_size = input ("enter the size of the book ")
            book = EBook (book_id, book_name, author_name, file_size)
        
        else:
            print("Invalid Choice")
            return
        
        self.books.append (book)
        

    def create_user (self):
        user_id = input ("enter the id of user")
        name = input ("enter the name of user")

        user = User (user_id, name)

        self.users.append (user)

    def borrow_book(self):
        book_id = int( input ("enter the book_id you want to borrow") )
        user_id =input ("enter the user_id")
        for book in self.books:
            if book.book_id == book_id and not book.is_borrowed:
                book.is_borrowed = True
                for u in self.users:
                    if u.user_id == user_id:
                        u.borrowed_books.append (book_id)
                        print(" Book borrowed successfully")
                        return
                print ("user not found") 
                return
        return
    
    def return_book(self):
        book_id = int (input ("enter the book_id you want to return"))
        user_id =input ("enter the user_id")
        for book in self.books:
            if book.book_id == book_id and book.is_borrowed:
                book.is_borrowed = False
                for u in self.users:
                    if u.user_id == user_id:
                        u.borrowed_books.remove (book_id)
                        print(" Book removed successfully")
                        return
                print ("user not found")
                return 
    
        return
    def search_book(self):
        keyword = input("enter the keyword")
        results = []
        for book in self.books:
            if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower():
                results.append(book)
        for r in results:
            r.display()


def main():
    
    lib =Library()
    lib.load_data()
    while True:
        print("select the operation you want to perform \n 1. printed all the books\n 2. create new books\n 3.view all users\n 4.Create new user \n 5. borrow a book\n 6. return book\n 7. search book\n  8. save the data\n 9.exit")


        work = int (input ("enter your choice"))
        match work:
            case 1:
                lib.view_books()
            case 2:
                lib.create_book()
            case 3:
                lib.userview()
            case 4:
                lib.create_user()
            case 5:
                lib.borrow_book()
            case 6:
                lib.return_book()
            case 7:
                lib.search_book()
            case 8:
                lib.save_data()
            case 9:
                return 




main()
        



