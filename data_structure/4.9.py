# 9. Create a program that uses a dictionary to implement a phonebook.

def display_menu():
    print("\nPhonebook Menu:")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Display All Contacts")
    print("5. Exit")

def add_contact(phonebook, name, number):
    phonebook[name] = number
    print(f"Contact '{name}' added successfully.")

def search_contact(phonebook, name):
    if name in phonebook:
        print(f"{name}: {phonebook[name]}")
    else:
        print(f"Contact '{name}' not found.")

def delete_contact(phonebook, name):
    if name in phonebook:
        del phonebook[name]
        print(f"Contact '{name}' deleted successfully.")
    else:
        print(f"Contact '{name}' not found.")

def display_contacts(phonebook):
    if phonebook:
        print("\nAll Contacts:")
        for name, number in phonebook.items():
            print(f"{name}: {number}")
    else:
        print("Phonebook is empty.")

# Main program
def phonebook_app():
    phonebook = {}
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            name = input("Enter name: ")
            number = input("Enter phone number: ")
            add_contact(phonebook, name, number)
        elif choice == '2':
            name = input("Enter name to search: ")
            search_contact(phonebook, name)
        elif choice == '3':
            name = input("Enter name to delete: ")
            delete_contact(phonebook, name)
        elif choice == '4':
            display_contacts(phonebook)
        elif choice == '5':
            print("Exiting phonebook. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

phonebook_app()
