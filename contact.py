contacts = {}

while True:
    print("\n Contact book")
    print("1. Create contact")
    print("2. Update contact")
    print("3. Delete contact")
    print("4. Search contact")
    print("5. Count contact")
    print("6. View contact")
    print("7. Exit")

    selection = input("Make your choice: ")

    if selection == "1":
        name = input("Write your name and surname: ")
        if name in contacts:
            print(f"This contacts {name} already exists")
        else:
            age = input("Enter age: ")
            email = input("Enter email: ")
            mobile_number = input("Enter mobil number: ")
            contacts[name] = {"age": int(
                age), "email": email, "Mobile number": mobile_number}
            print(f"Contact {name} successfully added")

    elif selection == "2":
        name = input("Enter the name of the contact you want to update: ")
        if name in contacts:
            age = input("Enter update age: ")
            email = input("Enter update email: ")
            mobile_number = input("Enter update mobil number: ")
            contacts[name] = {"age": int(
                age), "email": email, "Mobile number": mobile_number}
        else:
            print("Contact not found")

    elif selection == "3":
        name = input("Enter name of the contact you want to delete: ")
        if name in contacts:
            del contacts[name]
            print(f"The contact {name} deleted")
        else:
            print("Contact not found")

    elif selection == "4":
        s_name = input("Enter contact name to search: ")
        search = False
        for name, contact in contacts.items():
            if s_name.lower() in name.lower():
                print(
                    f"Found: Name {name}, Age {age}, Mobile number {mobile_number}, Email {email}  ")
                search = True
            if not search:
                print(f"The contact with name: {s_name} not found")

    elif selection == "5":
        print(f"Total contacts in your book: {len[contacts]}")

    elif selection == "6":
        name = input("Enter contact name to view: ")
        if name in contacts:
            contact = contacts[name]
            print(f"Name: {name}, Age:{age}, Mobile Number:{mobile_number}")
        else:
            print(f"No contact found, check the name you wrote {name}")

    elif selection == "7":
        print("Good bye, the program closing")
        break

    else:
        print("You chose a choice that does not exist")
