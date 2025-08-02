directory_items = []
while True:
    menu_option = input("Wellcome to our contactbook"
          +"\n 1 Add new contact"
           "\n 2 List existing contacts"
           "\n 3 Exit \n")

    dictionary_keys = ["Name", "Phone", "Email"]
    new_contact = {}

    if menu_option == "1":
        for key in dictionary_keys:
            new_contact[key] = input("Enter your " + key + " : ")
        directory_items.append(new_contact)

    elif menu_option == "2":
        for contact in directory_items:
            print(f"Name: {contact['Name']}")
            print(f"Phone: {contact['Phone']}")
            print(f"Email: {contact['Email']}\n")

    elif menu_option == "3":
        print("Goodbye")
        break

    else:
        print("Wrong input, choose 1, 2 or 3")
        continue