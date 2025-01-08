import json
import os

def load_contacts(filename="contacts.json"):
    if not os.path.exists(filename):
        return {}
    with open(filename, "r") as file:
        return json.load(file)

def save_contacts(contacts, filename="contacts.json"):
    with open(filename, "w") as file:
        json.dump(contacts, file, indent=4)
        print("Changes saved successfully!")
        
def add_contact(contacts):
    name = input("Enter the contact's name: ")
    if name in contacts:
        print(f"A contact with the name '{name}' already exists.")
        return

    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email (optional): ")

    contacts[name] = {
        "phone": phone,
        "email": email
    }
    print(f"Contact '{name}' added successfully!")
def view_contacts(contacts):
    if not contacts:
        print("No contacts found in the contact book.")
        return

    print("\n--- Contact List ---")
    for x, (name, info) in enumerate(contacts.items(), start=1):
        print(f"{x}. Name: {name}")
        print(f"   Phone: {info['phone']}")
        print(f"   Email: {info['email'] if info['email'] else 'N/A'}")


def search_contact(contacts):
    name = input("Enter the name of the contact to search: ")
    if name in contacts:
        info = contacts[name]
        print("\n--- Contact Found ---")
        print(f"Name: {name}")
        print(f"Phone: {info['phone']}")
        print(f"Email: {info['email'] if info['email'] else 'N/A'}")
    else:
        print(f"Contact '{name}' not found in the contact book.")


def update_contact(contacts):
    name = input("Enter the name of the contact to update: ")
    if name not in contacts:
        print(f"Contact '{name}' not found.")
        return

    print("\nWhat would you like to update?")
    print("1. Phone Number")
    print("2. Email")
    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        new_phone = input("Enter the new phone number: ")
        contacts[name]["phone"] = new_phone
        print(f"Contact '{name}' updated successfully!")
    elif choice == "2":
        new_email = input("Enter the new email: ")
        contacts[name]["email"] = new_email
        print(f"Contact '{name}' updated successfully!")
    else:
        print("Invalid choice. No changes made.")

def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully!")
    else:
        print(f"Contact '{name}' not found.")

def main():
    filename = "contacts.json"
    contacts = load_contacts(filename)

    while True:
        print("\n--- Contact Book ---")
        print("1. Add a New Contact")
        print("2. View All Contacts")
        print("3. Search for a Contact")
        print("4. Update a Contact")
        print("5. Delete a Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            save_choice = input("Do you want to save changes before exiting? (y/n): ")
            if save_choice == "yes":
                save_contacts(contacts, filename)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
