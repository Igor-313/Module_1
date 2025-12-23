contacts = {}

try:
    file = open("data.txt", "r", encoding="UTF-8")
    """потрібно щоб перед запуском циклу програма прочитала наявні контакти"""
    for line in file:
        if line.split():
            data = line.split(" | ")
            contacts[data[0]] = {"name": data[0], "age": int(
                data[1]), "email": data[2], "Mobile number": data[3].strip()}
    file.close()
except FileNotFoundError:
    file = open("data.txt", "w", encoding="UTF-8")
    file.close()


def save_data(contacts_dict):
    """Функція, яка перезаписує файл data.txt актуальними даними"""
    file = open("data.txt", "w", encoding="utf-8")
    for name, info in sorted(contacts_dict.items()):
        line = f"{info['name']} | {info['age']} | {info['email']} | {info['Mobile number']}\n"
        file.write(line)
    file.close()


while True:

    try:
        print("\nContact book:\n1. Create contact\n2. Update contact\n3. Delete contact\n4. Search contact\n5. View all contact\n6. Exit")

        selection = input("Make your choice: ")

        if selection == "1":
            name = input("Write your name and surname: ")
            if name in contacts:
                print(f"This contacts {name} already exists")
            else:
                age = input("Enter age: ")
                email = input("Enter email: ")
                if "@" not in email:
                    print("Error Invalid email (missing @) try again!")
                    continue
                mobile_number = input("Enter mobil number: ")
                if not (mobile_number.isdigit() and len(mobile_number) == 12):
                    print("Error: Mobile number must contain exactly 12 digits!")
                contacts[name] = {"name": name, "age": int(
                    age), "email": email, "Mobile number": mobile_number}

                contacts[name] = {
                    "name": name,
                    "age": int(age),
                    "email": email,
                    "Mobile number": mobile_number
                }
                save_data(contacts)

                print(f"Contact {name} successfully added")

        elif selection == "2":
            name_s = input(
                "Enter the name of the contact you want to update: ")
            if name_s in contacts:
                print(f"Contact {name_s} found. Enter new details.")
                new_name = input("Enter update name: ")
                age = input("Enter update age: ")
                email = input("Enter update email: ")
                mobile_number = input("Enter update mobile number: ")

                if new_name != name_s:
                    contacts[new_name] = {
                        "name": new_name,
                        "age": int(age),
                        "email": email,
                        "Mobile number": mobile_number
                    }
                    """видаляєм старе імя"""
                    del contacts[name_s]
                else:
                    """це потрібно якщо імя залтшається незмінним"""
                    contacts[name_s] = {
                        "name": name_s,
                        "age": int(age),
                        "email": email,
                        "Mobile number": mobile_number
                    }

                """визиваємо функцію для презапису контакту"""
                save_data(contacts)

                print(f"Contact {name_s} updated successfully!")
            else:
                print("Contact not found")

        elif selection == "3":
            name = input("Enter name of the contact you want to delete: ")
            if name in contacts:
                del contacts[name]
                save_data(contacts)
                print(f"The contact {name} deleted")
            else:
                print("Contact not found")

        elif selection == "4":
            s_name = input("Enter contact name to search: ")
            search = False
            for name, contact in contacts.items():
                if s_name == name:
                    print(
                        f"Name: {contact['name']}, Age: {contact['age']}, Email: {contact['email']}, Phone: {contact['Mobile number']}")
                    search = True
            if not search:
                print(f"The contact with name: {s_name} not found")

        elif selection == "5":
            file = open("data.txt", "r", encoding="utf-8")
            for line in sorted(file):
                print(line)
            file.close()

        elif selection == "6":
            print("Good bye, the program closing")
            break

        else:
            print("You chose a choice that does not exist")
    except ValueError as e:
        print(f"Value error: {e}")
    except KeyError as e:
        print(f"Key error: {e}")
    except NameError as e:
        print(f"Name error: {e}")
    except TypeError as e:
        print(f"There was a data type error: {e}")
