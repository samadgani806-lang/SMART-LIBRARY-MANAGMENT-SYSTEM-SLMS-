from SERVICES.EDIT_MEMBER_SERVICE import *
from SERVICES.MEMBER_SERVICE import *
from UTILES.HELPER import *
from UTILES.CONSTANT import *
from SERVICES.BOOK_SERVICE import *
def show_header():
    print ("#" * 60)
    print (f"{APP_NAME:^60}")
    print (f"Version: {VERSION:^60}")
    print ("#" * 60)
def owner():
    print ("made by sama - Ganikal")

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
   

def book_management_menu():
    

           
         
                 
 def edit_book():
     print ("\nEdit Book")

     
     
      

 def delete_books():
            print ("\nDelete book")




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
            print ("\nEdit Book")

        elif choice == "4":
            print("\nDelete Book")

        elif choice == "5":
            break

        else:
            print("\nInvalid Option.")

        input("\nPress Enter to continue...")


def member_management_menu():

 while True:
        print("\n" + "=" * 40)
        print("MEMBER MANAGMENT")
        print("=" * 40)

        print("1. Add Member")
        print("2. View Member")
        print("3. Edit Member")
        print("4. Delete Member")
        print("5. Back")

        choice = input("\nChoose an option: ")

        if choice == "1":
           add_member()

        elif choice == "2":
            view_member()

        elif choice == "3":
            edit_member()

        elif choice == "4":
            print("\nDelete Member")

        elif choice == "5":
            break

        else:
            print("\nInvalid Option.")

        input("\nPress Enter to continue...")



