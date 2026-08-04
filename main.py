

from UTILES.HELPER import *
from SERVICES.BOOK_SERVICE import *
from config import BOOKS_FILE
from SERVICES.STORAGE_SERVICE import *
from UTILES.MENU import *
library_name = ("welcome to Smart Library Managment System(SMLS)")
version = 1.0

#create a json file
#Function to create ID
# def create_ID():
#    if not books:
#       return "BK1001"

#    HIGHEST_ID = max(int (book["ID"][2:]) for book in books)
#    return f"BK{HIGHEST_ID + 1}"


#json function

                                                             

owner()

#mnu

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


   input("press Enter to continue......."),

    
   

