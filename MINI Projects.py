# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 21:08:52 2024

@author: Hp
"""

contacts = {}

def add_contact(name, phone, email):
    contacts[name] = {"phone": phone, "email": email}

def view_contacts():
    for name, details in contacts.items():
        print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")

def delete_contact(name):
    if name in contacts:
        del contacts[name]

while True:
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Delete Contact")
    print("4. Exit")
    
    choice = input("Enter choice: ")

    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        add_contact(name, phone, email)
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        name = input("Enter name to delete: ")
        delete_contact(name)
        print("Contact is Deleted")
    elif choice == '4':
        break
    else:
        print("Invalid choice")
