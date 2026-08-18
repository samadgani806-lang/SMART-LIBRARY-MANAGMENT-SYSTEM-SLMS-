from UTILES.HELPER import *
from SERVICES.BOOK_SERVICE import *
from config import BOOKS_FILE
from SERVICES.STORAGE_SERVICE import *
from UTILES.MENU import *

#create a json file
#Function to create ID


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

    
   

