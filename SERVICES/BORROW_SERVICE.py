from SERVICES.MEMBER_SERVICE import *
from SERVICES.BOOK_SERVICE import *
def check_book_exists(book_id):
    for book in books:
        if book["ID"] == book_id:
            return print(f"Book with ID {book_id} exists.")
    return print(f"Book with ID {book_id} does not exist.")





