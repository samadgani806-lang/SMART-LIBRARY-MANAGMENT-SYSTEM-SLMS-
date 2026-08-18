import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_DIR = os.path.join(BASE_DIR,"DATABASE")
BOOKS_FILE = os.path.join(DATABASE_DIR, "books.json")
MEMBERS_FILE = os.path.join(DATABASE_DIR, "members.json")
