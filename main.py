import json              
library_name = ("welcome to Smart Library Managment System(SMLS)")
version = 1.0
books = []
#create a json file
#function to create ID
# def create_ID():
#    if not books:
#       return "BK1001"

#    HIGHEST_ID = max(int (book["ID"][2:]) for book in books)
#    return f"BK{HIGHEST_ID + 1}"


#json function
def save_books():
    with open("books.json","w") as file:
         json.dump(books, file,indent=4)
def load_books():
    global books

    try:
        with open("books.json", "r") as file:
             books = json.load(file)

    except FileNotFoundError:
         books = []                                                              
def clearscreen ():
   import os
   os.system("cls"if os.name == "nt" else "clear")
v = "sama - Ganikal"
def show_header():
    print ("#" * 60)
    print ("SMART LIBRARY MANAGMENY SYSTEM")
    print ("#" * 60)
print ("made by ",v)

#mnu
def show_menu():
 print  ("1. Book Management")
 print ("2. Member Management")
 print ("3. Borrow Book")
 print ("4. Return Book")
 print ("5. Search")
 print ("6. Reports")
 print ("7. Backup Database")
 print ("8. Restore Database")
 print ("9. About Us")
 print ("10. Exit")
   


#def book_management_menu():
    

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
       save_books()
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
         
                 
 def edit_book():
      

  def delete_books():
            print ("\nDelete book")


 load_books()
    
 while True:
        print("\n" + "=" * 40)
        print("BOOK MANAGEMENT")
        print("=" * 40)

        print("1. Add Book")
        print("2. View Books")
        print("3. Edit Book")
        print("4. Delete Book")
        print("5. Back")

        choice = input("\nChoose an option: ")

        if choice == "1":
            Add_books()

        elif choice == "2":
             View_books()

        elif choice == "3":
            print("\nEdit Book")

        elif choice == "4":
            print("\nDelete Book")

        elif choice == "5":
            break

        else:
            print("\nInvalid Option.")

        input("\nPress Enter to continue...")



 
        


#main mnu
while True:
   clearscreen()
   show_header()
   show_menu()
     

   choice  = input("Choose an option. ")
   if choice  == "1":
      book_management_menu()
   elif choice  == "2":
      print ("Member Managment")
   elif  choice  == "3":
      print ("Borrow Book")
   elif choice  == "4":
      print ("Return Book")
   elif choice  == "5":
      print ("Searh")
   elif choice  == "7":
      print ("Report")
   elif choice  == "8":
      print ("Backup Database")
   elif choice  == "9":
      print ("About us")
   elif choice  == "10":
      print ("Exit")
      print ("Thank you for using SLMS")
      break
   else:
      print ("Invalid Option")


   input("press Enter to continue.......")
   

