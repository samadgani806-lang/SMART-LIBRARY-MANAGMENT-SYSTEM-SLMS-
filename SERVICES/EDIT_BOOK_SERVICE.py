from config import BOOKS_FILE
from SERVICES.STORAGE_SERVICE import load_data, save_data

def edit_book():
    books = load_data(BOOKS_FILE)
    book_id = input("Enter the ID of the book you want to edit: ")
    for book in books:
        if book["ID"] == book_id:
            print("Editing Book:", book["TITLE"])
            title = input("Enter new title (leave blank to keep current): ")
            author = input("Enter new author (leave blank to keep current): ")
            category = input("Enter new category (leave blank to keep current): ")
            year = input("Enter new year (leave blank to keep current): ")
            copies = input("Enter new copies (leave blank to keep current): ")

            if title:
                book["TITLE"] = title
            if author:
                book["AUTHOR"] = author
            if category:
                book["CATEGORY"] = category
            if year:
                book["YEAR"] = year
            if copies:
                book["COPIES"] = copies
                # Update available copies based on the new total copies
                borrowed_copies = int(book["COPIES"]) - int(book["AVALIBLE COPIES"])
                book["AVALIBLE COPIES"] = str(int(copies) - borrowed_copies)

            save_data(BOOKS_FILE, books)
            print("Book updated successfully.")
            return
    print("Book not found.")


def delete_book():
    books = load_data(BOOKS_FILE)
    book_id = input("Enter the ID of the book you want to delete: ")
    for book in books:
        if book["ID"] == book_id:
            books.remove(book)
            save_data(BOOKS_FILE, books)
            print("Book deleted successfully.")
            return
    print("Book not found.")