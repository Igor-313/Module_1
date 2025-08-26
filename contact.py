contacts= {}

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
        else: #доповнити інформацію ниже
            age = input()
            email = input()
            mobile_number = input()
            contacts[name] = {"age":int(age), "email":email, "Mobile number":mobile_number}
            print(f"Contact {name} successfully added")

    elif selection == "2":
        name = input("Enter the name of the contact you want to update: ")
    #добавити input з 1. + contacts[name] + not found contact.
        if name in contacts:
            pass
        else:
            pass
    
    elif selection == "3":
        pass
        
    elif selection == "4":
        pass

    elif selection == "5":
        pass
    
    elif selection == "6":
        name = input("Enter contact name to view: ")
        if name in contacts:
            contact = contacts[name]
            print(f"Name: {name}, Age:{age}, Mobile Number:{mobile_number}")
        else:
            print(f"No contact found, check the name you wrote {name}")
    
    elif selection == "7":
        pass