contact_book = []
def list_add(list):
    user_name = str(input("name"))
    user_phone = int(input("phone"))
    data = {"name" : user_name, "phone" : user_phone}
    for i in contact_book:
        if i["name"] == user_name and i["phone"] == user_phone:
            print("This name and phone number already exist in the contact book.")
            return
    contact_book.append(data)

def list_search(list):
    search_name = input("Enter the name to search: ")
    search_phone = input("Enter the phone number to search: ")
    for i in contact_book:
        if i["name"] == search_name and i["phone"] == search_phone:
            print("Contact found:", i)
            return
    print("Contact not found.")

def list_update(list):
    search_update_name = input("Enter the name to update: ")
    search_update_phone = input("Enter the phone number to update: ")
    for i in contact_book:
        if i["name"] == search_update_name and i["phone"] == search_update_phone:
            new_name = input("Enter the new name: ")
            new_phone = input("Enter the new phone number: ")
            i["name"] = new_name
            i["phone"] = new_phone
            print("Contact updated:", i)
            return
    print("Contact not found.")

def list_delete(list):
    search_delete_name = input("Enter the name to delete: ")
    search_delete_phone = input("Enter the phone number to delete: ")
    for i in contact_book:
        if i["name"] == search_delete_name and i["phone"] == search_delete_phone:
            contact_book.remove(i)
            print("Contact deleted:", i)
            return
    print("Contact not found.")

def list_contact(list):
    if not contact_book:
        print("No contacts found.")
    else:
        print("Contact List:")
        for i in contact_book:
            print(i)


def exit_program():
    print("Exiting the program.")
    




def main():
    while True:
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. List Contacts")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            list_add(contact_book)
        elif choice == "2":
            list_search(contact_book)
        elif choice == "3":
            print(contact_book)
        elif choice == "4":
            list_update(contact_book)
        elif choice == "5":
            list_delete(contact_book)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

main()