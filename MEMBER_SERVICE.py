from config import MEMBERS_FILE
from SERVICES.STORAGE_SERVICE import *

members = load_data(MEMBERS_FILE)
def member_management_menu():


#ask for input

#book_id = generate_book_id(books, BOOK_ID_PREFIX, BOOK_START_ID)

 def add_member():
    member_id = input("MEMBER ID: ")                         
    name = input("NAME: ")
    class_ = input ("CLASS: ")
    age  = input("AGE: ")
    branch = input("BRANCH: ")
    member = {
           

     "ID" : member_id,
     "NAME" : name,
     "CLASS" : class_,
     "AGE" : age,
     "BRANCH" : branch,

           
       }
    members.append(member)
    save_data(MEMBERS_FILE, members)
print("MEMBER ADDED SUCCESFULLY")

def view_member():
    print (" VIEW MEMBER ")
    print ("_"*30)
    for member in members:
        print ("Member ID: ",member["ID"])
        print("Name: ",member["NAME"])
        print ("Class: ",member["CLASS"])
        print ("Age: ",member["AGE"])
        print ("Branch: ",member["BRANCH"])
        if len(members) == 0:
            print("There are no more members , PLEASE COME BACK LATER")
            return