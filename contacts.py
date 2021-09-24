# store the contact added by users and check for duplicates.
from replit import db

def phoneBook(name, number):
  if name in db:
    print("Name already exist. Try with a different name.")
  else:
    db[name] = number  

# check from the phoneBook.
def contactsBook(name):
  number = db.get(name)
  return number

# Search for contacts
def search_contacts(search):
  match_keys = db.prefix(search)
  return {k: db[k] for k in match_keys}

# update contact
def upContact(old_name,new_name,new_number):
  db[new_name] = new_number
  del db[old_name]

# update number
def upNumber(old_name, new_number):
  db[old_name] = new_number  

# Show all the contacts
def showAll():
  for key in db.keys():
    print (f"Name: {key} \nNumber:{db[key]}\n")     

# Delete contact
def delContact(name):
  del db[name]  
  
