
import json
import re

contacts = {}

def welcome_message():
    print("Welcome to the Contact Management System!")

def menu_options():
    print("Menu: \n 1. Add a new contact \n 2. Edit an existing contact \n 3. Delete a contact \n 4. Search for a contact \n 5. Display all contacts \n 6. Export contacts to a text file \n 7. Quit \n")   

def confirm_phone(phone):
    return re.match(r'^\+?\d{10,15}$', phone)

def confirm_email(email):
    return re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email)

def add_contact():
    print("Add a new contact. ")

    name = input("Enter name: ")
    phone = input("Enter phone number (xxxxxxxxxx): ")

    if not confirm_phone(phone):
        print("Invalid format. Please try again. ")
        return
    
    email = input("Enter email address: ")

    if not confirm_email(email):
        print("Invalid format. Please try again. ")
        return
    
    additional_info = input("Enter additional info: (address, notes, ect. )")
    
    contacts[phone] = {
        'name' : name,
        'email' : email,
        'additional_info': additional_info
    }
    print(f"Contact {name} has been added. ")


def edit_contact():
    phone = input("Please enter the phone number of the contact you would like to edit: ")
    if phone not in contacts:
        print("Contact not found. ")
        return

    print("Updating contact... ")
    name = input("Enter updated name: ")
    email = input ("Enter updated email:  ")
    additional_info = input("Enter updated additional information: ")

    if name:
        contacts[phone]['name'] = name
    if email and confirm_email(email):
        contacts[phone]['email'] = email
    if additional_info:
        contacts[phone]['additional_info'] = additional_info

    print("Contact has been updated. ")


def delete_contact():
    phone = input("Please enter the phone number of the contact you would like to delete: ")
    if phone in contacts:
        del contacts[phone]
        print("Contact has been deleted. ")
    else:
        print("Contact not found. ")


def search_contact():
    phone = input("Enter the phone number of the contact you would like to search: ")
    if phone in contacts:
        contact = contacts[phone]
        print(f"Name: {contact['name']}")
        print(f"Phone: {phone}")
        print(f"Email: {contact['email']}")
        print(f"Additional Info: {contact['additional_info']}")

    else:
        print("Contact not found. ")


def display_contacts():
    if not contacts:
        print("No contacts available. ")
        return
    for phone, details in contacts.items():
        print(f"Name: {details['name']}, Phone: {phone}, Email: {details['email']}, Additional Info: {details['additional_info']} ")
        

def export_contacts():
    filename = input("Enter filename to export contacts: (i.e, contacts.json)")
    try:
        with open(filename, 'w') as f:
            json.dump(contacts, f, indent=4)
        print(f"Contacts exported to {filename} successfully. ")
    except Exception as e:
        print(f"An error occurred: {e}")


def import_contacts():
    filename = input("Enter filename to import contacts from: (i.e, contacts.json) ")
    try:
        with open(filename, 'r') as f:
            imported_contacts = json.load(f)
            contacts.update(imported_contacts)
        print(f"Contacts imported from {filename} successfully. ")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    welcome_message()

    while True:
        menu_options()
        option = input("Please choose an option (1-7): ")

        if option == '1':
            add_contact()
        elif option == '2':
            edit_contact()
        elif option == '3':
            delete_contact() 
        elif option == '4':
            search_contact()
        elif option == '5':
            display_contacts()
        elif option == '6':
            export_contacts()
        elif option == '7':
            print("Thank you for using the Contact Management System! ")
            break
        else:
            print("Invalid option, please try again. ")


if __name__ == "__main__":
    main()
