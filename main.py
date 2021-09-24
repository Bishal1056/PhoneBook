#Using built in database of replit.

import contacts
from replit import db
from os import system

# option to choose
main_message = """WELCOME TO PHONEBOOK

--------------------------------------

What you want to do today?
1 - Add a new contact.
2 - Find a contact.
3 - Update a contact.
4 - Show all contacts.
5 - Delete a contact.

---------------------------------------

"""

#add contact by users
def add_contact():
  name = input("Please enter the contact's name: ")
  number = input("Please enter the contact's phone number: ")

  print(f"Adding {name} with {number}")
  contacts.phoneBook(name, number)

#retrieve contact by users if exists
def get_contact():
  name = input("Please enter the contact's name to find: ")
  number = contacts.contactsBook(name)
  if number:
    print(f"{name}'s number is {number}")
  else:
    matches = contacts.search_contacts(name)
    if matches:
      for k in matches:
        print(f"{k}'s number is {matches[k]}")
    else:    
      print(f"Contact {name} does not exist")

# Update contact. 
# 1. change name keep the number.
# 2. Change number keep the name.
def update_contact():
  old_name = input("Please enter the old name to update: ")
  old_number = contacts.contactsBook(old_name)
  if old_number:
    new_name = input(f"Please enter the new name for this contact (leave blank to keep {old_name}): ").strip()
    new_number = input(f"Please enter the new number for this contact (leave blank to keep {old_number}): ").strip()

    if not new_number:
      new_number = old_number
    if not new_name:
      contacts.upNumber(old_name,new_name)
    else:
      contacts.upContact(old_name,new_name,new_number)      
    
  else:
    print(f"Contact named {old_name} does not exist") 

# Show all contacts
def show_contacts():
  print("Showing all contacts")
  contacts.showAll()  

# Delete contact
def delete_contact():
  name = input("Please enter the contact's name to delete: ")
  contact = contacts.contactsBook(name)
  if contact:
    print(f"Deleting {name}")
    contacts.delContact(name)
  else:
    print(f"This contact named {name} does not exist")  


# main function
def main():
  print(main_message)
  choice = input("Please make your choice: ").strip()
  if choice == "1":
    add_contact()
  elif choice == "2":
    get_contact() 
  elif choice == "3":
    update_contact()  
  elif choice == "4":
    show_contacts() 
  elif choice == "5":
    delete_contact()    

  else:
    print("Invalid input. Please try again.")
    

# keep the phoneBook runing as long as user wants.
while True:
  system("clear")
  main()
  input("Press enter to continue: ")      