from config import BOOKS_FILE
from SERVICES.STORAGE_SERVICE import *

books = load_data(BOOKS_FILE)
def Add_books():
       print("ADD NEW BOOKS")
       print("-"* 30)
       #ask for input
       book_id = input("ID: ")
       titl = input("TITLE: ")
       author = input("AUTHOR: ")
       category = input("CATEGORY: ")
       year = input("YEAR: ")
       copies = input("COPIES: ")
       book = {
           
           "ID" : book_id,
           "TITLE" : titl,
           "AUTHOR" : author,
           "CATEGORY" : category,
           "YEAR" : year,
           "COPIES" : copies,
           "AVALIBLE COPIES" : copies,
           "TIMES BORROWED" : 0,

           
       }
       books.append(book)
       save_data(BOOKS_FILE, books)
       print("BOOK ADDED SUCCESFULLY")


 
 
 
 
 
 
 
 
def View_books():
      print (" VIEW BOOKS ")
      print ("_"*30)
      for book in books:
          print ("Book ID: ",book["ID"])
          print("title: ",book["TITLE"])
          print ("Author: ",book["AUTHOR"])
          print ("Category: ",book["CATEGORY"])
          print ("Copies: ",book["COPIES"])
          print ("Avalible Copies: ",book["AVALIBLE COPIES"])
          if len(books) == 0:
                 print("There are no more books , PLEASE COME BACK LATER")
                 return
