contacts = {}


while True:
    try:
        print("\nContact book:\n1. Create contact\n2. Update contact\n3. Delete contact\n4. Search contact\n5. View contact\n6. Exit")

        selection = input("Make your choice: ")

        if selection == "1":
            name = input("Write your name and surname: ")
            if name in contacts:
                print(f"This contacts {name} already exists")
            else:
                file = open("data.txt", "a", encoding="utf-8")
                age = input("Enter age: ")
                email = input("Enter email: ")
                mobile_number = input("Enter mobil number: ")
                contacts[name] = {"age": int(
                    age), "email": email, "Mobile number": mobile_number}
                print(f"Contact {name} successfully added")
                file.write(f"{name} | {age} | {email} | {mobile_number} \n")
                file.close()

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
            file = open("data.txt", "r")
            for line in file:
                print(line)
            file.close()

        elif selection == "6":
            print("Good bye, the program closing")
            break

        else:
            print("You chose a choice that does not exist")
    except ValueError:
        print()
