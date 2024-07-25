class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email, address):
        if name in self.contacts:
            print(f"Contact '{name}' already exists.")
            return
        self.contacts[name] = {
            'phone': phone,
            'email': email,
            'address': address
        }
        print(f"Contact '{name}' added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("Contact list is empty.")
            return
        print("\nContact List:")
        for name, details in self.contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}")

    def search_contact(self, search_term):
        results = [
            (name, details) for name, details in self.contacts.items()
            if search_term.lower() in name.lower() or search_term in details['phone']
        ]
        if not results:
            print(f"No contacts found for '{search_term}'.")
            return
        print("\nSearch Results:")
        for name, details in results:
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")

    def update_contact(self, name, phone=None, email=None, address=None):
        if name not in self.contacts:
            print(f"Contact '{name}' does not exist.")
            return
        if phone:
            self.contacts[name]['phone'] = phone
        if email:
            self.contacts[name]['email'] = email
        if address:
            self.contacts[name]['address'] = address
        print(f"Contact '{name}' updated successfully!")

    def delete_contact(self, name):
        if name not in self.contacts:
            print(f"Contact '{name}' does not exist.")
            return
        del self.contacts[name]
        print(f"Contact '{name}' deleted successfully!")

    def display_interface(self):
        print("\n--- Contact Book ---")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

    def run(self):
        while True:
            self.display_interface()
            choice = input("Enter your choice (1-6): ")
            if choice == '1':
                name = input("Enter name: ")
                phone = input("Enter phone number: ")
                email = input("Enter email address: ")
                address = input("Enter address: ")
                self.add_contact(name, phone, email, address)
            elif choice == '2':
                self.view_contacts()
            elif choice == '3':
                search_term = input("Enter name or phone number to search: ")
                self.search_contact(search_term)
            elif choice == '4':
                name = input("Enter name of the contact to update: ")
                phone = input("Enter new phone number (leave blank to skip): ")
                email = input("Enter new email address (leave blank to skip): ")
                address = input("Enter new address (leave blank to skip): ")
                self.update_contact(name, phone or None, email or None, address or None)
            elif choice == '5':
                name = input("Enter name of the contact to delete: ")
                self.delete_contact(name)
            elif choice == '6':
                print("Exiting Contact Book. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")


# Create a ContactBook instance and run the application
contact_book = ContactBook()
contact_book.run()
