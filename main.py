import json

# Define a class for managing contacts
class ContactManager:
    def __init__(self, filename="contacts.json"):
        self.filename = filename
        self.contacts = self.load_contacts()

    # Load contacts from the file
    def load_contacts(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            return {}

    # Save contacts to the file
    def save_contacts(self):
        with open(self.filename, 'w') as file:
            json.dump(self.contacts, file, indent=4)

    # Add a new contact
    def add_contact(self, name, phone, email):
        if name in self.contacts:
            print("This contact already exists!")
        else:
            self.contacts[name] = {"phone": phone, "email": email}
            self.save_contacts()
            print(f"Contact {name} added successfully!")

    # View all contacts
    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for name, details in self.contacts.items():
                print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")

    # Edit an existing contact
    def edit_contact(self, name):
        if name not in self.contacts:
            print("Contact not found!")
        else:
            phone = input("Enter new phone number: ")
            email = input("Enter new email address: ")
            self.contacts[name] = {"phone": phone, "email": email}
            self.save_contacts()
            print(f"Contact {name} updated successfully!")

    # Delete a contact
    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()
            print(f"Contact {name} deleted successfully!")
        else:
            print("Contact not found!")

# Main function for the contact management program
def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add a new contact")
        print("2. View contacts")
        print("3. Edit a contact")
        print("4. Delete a contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter the contact's name: ")
            phone = input("Enter the contact's phone number: ")
            email = input("Enter the contact's email address: ")
            contact_manager.add_contact(name, phone, email)
        
        elif choice == '2':
            contact_manager.view_contacts()

        elif choice == '3':
            name = input("Enter the contact's name to edit: ")
            contact_manager.edit_contact(name)

        elif choice == '4':
            name = input("Enter the contact's name to delete: ")
            contact_manager.delete_contact(name)

        elif choice == '5':
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
