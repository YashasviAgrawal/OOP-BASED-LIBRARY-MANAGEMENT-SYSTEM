# OOP-Based Library Management System

A simple, object-oriented library management system written in Python. This project demonstrates basic OOP design with Books (Printed and EBook), Users, and a Library that supports creating users/books, borrowing and returning books, searching, and persistent storage to a JSON file.

Main script: [Main.py](https://github.com/YashasviAgrawal/OOP-BASED-LIBRARY-MANAGEMENT-SYSTEM/blob/63c2880b5351660ccd8837204b9fe20bfd040ba7/Main.py)

## Features
- Book model with two concrete subtypes:
  - PrintedBook (with page count)
  - EBook (with file size)
- User model tracking borrowed books
- Library actions:
  - Create books and users interactively
  - View books and users
  - Borrow and return books (tracks `is_borrowed` and user's `borrowed_books`)
  - Search books by title or author (case-insensitive substring match)
  - Save and load data to/from `library.json` for persistence

## Requirements
- Python 3.7+ (uses only standard library modules)

## Installation
1. Clone the repository:
```bash
git clone https://github.com/YashasviAgrawal/OOP-BASED-LIBRARY-MANAGEMENT-SYSTEM.git
cd OOP-BASED-LIBRARY-MANAGEMENT-SYSTEM
```

2. Run the program:
```bash
python Main.py
```

No external dependencies required.

## Usage
When you run `Main.py`, a text menu prompts for operations:

- 1 — Print all books
- 2 — Create new book (choose Printed or EBook)
- 3 — View all users
- 4 — Create new user
- 5 — Borrow a book (enter book_id and user_id)
- 6 — Return a book (enter book_id and user_id)
- 7 — Search book by keyword (title or author)
- 8 — Save data to `library.json`
- 9 — Exit

Example interactive session:
```
select the operation you want to perform 
 1. printed all the books
 2. create new books
 3.view all users
 4.Create new user 
 5. borrow a book
 6. return book
 7. search book
[...]

enter your choice: 2
 enter the book_id 101
enter the book name The Python Way
enter the author name Guido van Rossum
which kind of book 
 1. printed
 2. ebook: 1
enter the total number of pages: 320

enter your choice: 4
enter the id of user: u1
enter the name of user: Alice

enter your choice: 5
enter the book_id you want to borrow: 101
enter the user_id: u1
Book borrowed successfully
```

Notes:
- Book IDs are stored as integers in the code; user IDs are stored as strings.
- The program writes/reads `library.json` to persist books and users between runs.

## Data format (`library.json`)
Saved structure example:
```json
{
    "books": [
        {
            "type": "PrintedBook",
            "book_id": 101,
            "title": "The Python Way",
            "author": "Guido van Rossum",
            "is_borrowed": true,
            "pages": "320"
        },
        {
            "type": "EBook",
            "book_id": 102,
            "title": "Learning Algorithms",
            "author": "Jane Doe",
            "is_borrowed": false,
            "file_size": "2MB"
        }
    ],
    "users": [
        {
            "user_id": "u1",
            "name": "Alice",
            "borrowed_books": [
                101
            ]
        }
    ]
}
```
Important: `pages` and `file_size` in the current implementation are stored as the raw input strings (the program doesn't currently validate numeric values).

## Code overview
- Main classes:
  - `Book` — base class, stores `book_id`, `title`, `author`, `is_borrowed`
  - `PrintedBook(Book)` — adds `pages`
  - `EBook(Book)` — adds `file_size`
  - `User` — stores `user_id`, `name`, `borrowed_books` (list of book IDs)
  - `Library` — stores collections of books and users; handles persistence and all operations
- Key functions:
  - `Library.save_data()` — serializes books and users to `library.json`
  - `Library.load_data()` — recreates objects from `library.json`
  - Interactive methods: `create_book`, `create_user`, `borrow_book`, `return_book`, `search_book`, `view_books`, `userview`
## Contributing
Contributions are welcome. If you'd like to contribute:
1. Fork the repo
2. Create a feature branch
3. Make changes and add tests where appropriate
4. Open a pull request with a clear description of changes

## License
No license file is included in the repository. If you want to use or distribute this project, consider adding a LICENSE (for example, MIT License).

## Contact
Repository: [OOP-BASED-LIBRARY-MANAGEMENT-SYSTEM](https://github.com/YashasviAgrawal/OOP-BASED-LIBRARY-MANAGEMENT-SYSTEM)  
Main script: [Main.py](https://github.com/YashasviAgrawal/OOP-BASED-LIBRARY-MANAGEMENT-SYSTEM/blob/63c2880b5351660ccd8837204b9fe20bfd040ba7/Main.py)
