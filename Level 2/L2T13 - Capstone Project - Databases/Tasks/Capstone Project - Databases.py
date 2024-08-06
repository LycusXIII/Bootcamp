'''
This program is a book management system for an ebookstore it uses or
creates a database called 'ebookstore.db' and has various functions like
adding, searching or deleting books in the database.
'''
import sqlite3
import sys
import os
from tabulate import tabulate


def check_create_db():
    '''
    Check if the db exists if not it will be created and populated with
    data.
    Args:
        None
    Returns:
        db: the database connection.
    '''
    # Checks if db exists
    db_exists = os.path.exists('ebookstore.db')
    try:
        db = sqlite3.connect('ebookstore.db')
        cursor = db.cursor()
        if not db_exists:
            cursor.execute(
                '''CREATE TABLE book(id INTEGER PRIMARY KEY,
                title TEXT, author TEXT, qty INTEGER)''')
            db.commit()
        else:
            print("Connection to database established.")
        # Inserts data if db wasn't created before
        if not cursor.execute('''SELECT * FROM book''').fetchone():
            # Sample data.
            book_data = [
                (3001, "A Tale of Two Cities", "Charles Dickens", 30),
                (3002, "Harry Potter and the Philosopher's Stone",
                 "J.K. Rowling", 40),
                (3003, "The Lion, the Witch and the Wardrobe",
                 "C. S. Lewis", 25),
                (3004, "The Lord of the Rings", "J.R.R Tolkien", 37),
                (3005, "Alice in Wonderland", "Lewis Carroll", 12)]
            cursor.executemany(
                '''INSERT INTO book(id, title, author, qty)
                VALUES(?,?,?,?)''', book_data)
            db.commit()
            print("Database created and populated with sample data.")
        return db
    except sqlite3.Error as e:
        print(f"Error creating the database: {e}")


def enter_book(db):
    '''
    This functions adds a book to the database with user inputted information
    Args:
        db: is the database connection
    Return:
        None
    '''
    cursor = db.cursor()
    while True:
        try:
            title = input("Please enter the full title of the book:\n").strip()
            if not title:
                raise ValueError("Invalid input, please try again.")
            author = input("Please enter the authors name:\n").strip()
            if not author:
                raise ValueError("Invalid input, please try again.")
            cursor.execute('''SELECT * FROM book WHERE title = ?
                           AND author = ?''', (title, author))
            # Checks if the book exists
            if cursor.fetchone() is None:
                while True:
                    try:
                        qty = int(
                            input("Please enter the quantity:\n").strip())
                        if qty <= 0:
                            raise ValueError
                        break
                    except ValueError:
                        print("Invalid input, please enter a positive number.")
                # Adds the book to the book to the database
                cursor.execute('''INSERT INTO book (title, author, qty)
                    VALUES(?, ?, ?)''', (title, author, qty))
                db.commit()
                print(f"'{title}' book by {author} "
                      "was successfully added to database!")
            else:
                print(f"The book '{title}' by {author} "
                      "already exists within the database")
        except ValueError as error:
            print(error)
        break


def update_book(db):
    '''
    This function updates a books information or quantity based on user
    input to the database.
    Args:
        db: is the database connection
    Return:
        None
    '''
    cursor = db.cursor()
    cursor.execute('''SELECT * FROM book''')
    books = cursor.fetchall()
    print(tabulate(books, headers=["id", "title", "author", "qty"],
                   tablefmt='fancy_grid'))
    while True:
        try:
            search_id = int(input("Please enter the ID of the book you want "
                                  "to update:\n"))
            if search_id <= 0:
                raise ValueError
            cursor.execute('''SELECT * FROM book WHERE id = ?''', (search_id,))
            books = cursor.fetchall()
            if books:
                print(tabulate(books, headers=[
                    "id", "title", "author", "qty"
                    ], tablefmt='fancy_grid'))
                print()
                break
            else:
                print(f"No books was found with id number {search_id}: ")
                continue
        except ValueError:
            print("Invalid input, please enter a positive number.")

    while True:
        update_menu = input("Select one of the follow:\n"
                            "t - Update title\n"
                            "a - Update author\n"
                            "q - Update quantity\n"
                            "e - or return to main menu.\n"
                            ": ").lower()
        if update_menu == "t":
            update_title = input("Please enter the new title of the book:\n")
            # Checks if the input isn't empty
            if update_title.strip():
                cursor.execute('''UPDATE book SET title = ? WHERE id = ?''',
                               (update_title, search_id))
                db.commit()
                print(f"The title of {search_id} was updated to "
                      f"{update_title}")
                cursor.execute('''SELECT * FROM book WHERE id = ?''',
                               (search_id,))
                books = cursor.fetchall()
                print(tabulate(books, headers=["id", "title", "author", "qty"],
                               tablefmt='fancy_grid'))
                print()
            else:
                print("Invalid input, please try again.")
                continue
        elif update_menu == "a":
            update_author = input("Please enter the new author of the book:\n")
            # Checks if the input isn't empty
            if update_author.strip():
                cursor.execute('''UPDATE book SET author = ? WHERE id = ?''',
                               (update_author, search_id))
                db.commit()
                print(f"The author of {search_id} was updated to "
                      f"{update_author}")
                cursor.execute('''SELECT * FROM book WHERE id = ?''',
                               (search_id,))
                books = cursor.fetchall()
                print(tabulate(books, headers=["id", "title", "author", "qty"],
                               tablefmt='fancy_grid'))
                print()
        elif update_menu == "q":
            while True:
                try:
                    update_qty = int(input("Please enter the new quantity of "
                                           "the book:\n"))
                    if update_qty <= 0:
                        raise ValueError
                    break
                except ValueError:
                    print("Invalid input, please enter a positive number.")
            cursor.execute('''UPDATE book SET qty = ? WHERE id = ?''',
                           (update_qty, search_id))
            db.commit()
            print(f"The quantity of {search_id} was updated to "
                  f"{update_qty}")
            cursor.execute('''SELECT * FROM book WHERE id = ?''',
                           (search_id,))
            books = cursor.fetchall()
            print(tabulate(books, headers=["id", "title", "author", "qty"],
                           tablefmt='fancy_grid'))
            print()
        elif update_menu == "e":
            return
        else:
            print("Invalid choice please try again.")
            continue


def delete_book(db):
    '''
    This functions deletes a book based on user input from the database.
    Args:
        db: is the database connection
    Return:
        None
    '''
    cursor = db.cursor()
    cursor.execute('''SELECT * FROM book''')
    books = cursor.fetchall()
    print(tabulate(books, headers=["id", "title", "author", "qty"],
                   tablefmt='fancy_grid'))
    while True:
        try:
            search_id = int(input("Please enter the ID of the book you want "
                                  "to update:\n"))
            if search_id <= 0:
                raise ValueError
            cursor.execute('''SELECT * FROM book WHERE id = ?''', (search_id,))
            books = cursor.fetchall()
            if books:
                cursor.execute('''DELETE FROM book WHERE id = ?''',
                               (search_id,))
                db.commit()
                print(f"The book with ID of {search_id} "
                      "was successfully removed from the database")
                break
            else:
                print(f"No books was found with id number {search_id}: ")
        except ValueError:
            print("Invalid input, please enter a positive number.")


def search_book(db):
    '''
    This functions allow the user to search for a book by either searching
    by title or author or both.
    Args:
        db: is the database connection
    Return:
        None
    '''
    cursor = db.cursor()
    while True:
        search_menu = input("Select one of the follow:\n"
                            "t - search for book by title.\n"
                            "a - search for book by author.\n"
                            "b - search for book by title and author.\n"
                            "e - or return to main menu.\n"
                            ": ").lower()
        if search_menu == "t":
            while True:
                search_title = input("Please enter the title of the book:\n")
                # Checks if the input isn't empty
                if search_title.strip():
                    cursor.execute('''SELECT * FROM book WHERE title = ?''',
                                   (search_title,))
                    books = cursor.fetchall()
                    if books:
                        print(tabulate(books, headers=[
                            "id", "title", "author", "qty"
                            ], tablefmt='fancy_grid'))
                        print()
                        break
                    else:
                        print("No book was found with the title: "
                              f"{search_title}")
                        break
                else:
                    print("Invalid input please try again. (cannot be empty)")
        elif search_menu == "a":
            while True:
                search_author = input("Please enter the author of the book:\n")
                # Checks if the input isn't empty
                if search_author.strip():
                    cursor.execute('''SELECT * FROM book WHERE author = ?''',
                                   (search_author,))
                    books = cursor.fetchall()
                    if books:
                        print(tabulate(books, headers=[
                            "id", "title", "author", "qty"
                            ], tablefmt='fancy_grid'))
                        print()
                        break
                    else:
                        print("No books was found that was written by: "
                              f"{search_author}")
                        break
                else:
                    print("Invalid input please try again. (cannot be empty)")
        elif search_menu == "b":
            while True:
                search_title = input("Please enter the title of the book:\n")
                search_author = input("Please enter the author of the book:\n")
                # Checks if the both inputs isn't empty
                if search_title.strip() and search_author.strip():
                    cursor.execute('''SELECT * FROM book WHERE title = ?
                        AND author = ?''', (search_title, search_author))
                    books = cursor.fetchall()
                    if books:
                        print(tabulate(books, headers=[
                            "id", "title", "author", "qty"
                            ], tablefmt='fancy_grid'))
                        print()
                        break
                    else:
                        print("No books was found with title: "
                              f"{search_title} author: "
                              f"{search_author}")
                        break
                else:
                    print("Invalid input please try again. (cannot be empty)")
        elif search_menu == "e":
            return
        else:
            print("Invalid choice please try again.")
            continue


db = check_create_db()
while True:
    main_menu = input("Select one of the following:\n"
                      "1. Enter book\n"
                      "2. Update book\n"
                      "3. Delete book\n"
                      "4. Search books\n"
                      "0. Exit\n"
                      ": ").lower()
    if main_menu == '1':
        # This called the enter_book() function
        # and passes the db connection
        enter_book(db)
    elif main_menu == '2':
        # This called the update_book() function
        # and passes the db connection
        update_book(db)
    elif main_menu == '3':
        # This called the delete_book() function
        # and passes the db connection
        delete_book(db)
    elif main_menu == '4':
        # This called the search_book() function
        # and passes the db connection
        search_book(db)
    elif main_menu == '0':
        print("Closing the database and exiting program.")
        # Closes database
        db.close()
        # Stops the program.
        sys.exit(0)
    else:
        print("You have entered an invalid input. Please try again")
