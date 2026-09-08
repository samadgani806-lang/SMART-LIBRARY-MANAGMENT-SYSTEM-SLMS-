from config import MEMBERS_FILE
from SERVICES.STORAGE_SERVICE import load_data, save_data

def edit_member():
    members = load_data(MEMBERS_FILE)
    member_id = input("Enter the ID of the member you want to edit: ")
    for member in members:
        if member["ID"] == member_id:
            print("Editing Member:", member["NAME"])
            name = input("Enter new name (leave blank to keep current): ")
            class_ = input("Enter new class (leave blank to keep current): ")
            age = input("Enter new age (leave blank to keep current): ")
            branch = input("Enter new branch (leave blank to keep current): ")

            if name:
                member["NAME"] = name
            if class_:
                member["CLASS"] = class_
            if age:
                member["AGE"] = age
            if branch:
                member["BRANCH"] = branch

            save_data(MEMBERS_FILE, members)
            print("Member updated successfully.")
            return
    print("Member not found.")



def delete_member():
    members = load_data(MEMBERS_FILE)
    member_id = input("Enter the ID of the member you want to delete: ")
    for member in members:
        if member["ID"] == member_id:
            members.remove(member)
            save_data(MEMBERS_FILE, members)
            print("Member deleted successfully.")
            return
    print("Member not found.")