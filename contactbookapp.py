contact={}


def display_contact():
    print("Name\t\tContact number")
    for key in contact:
        print("{}\t\t{}".format(key,contact.get(key)))

while True:
    choice=int(input("1.Add new contact\n 2.Search contact\n 3.Display Contact\n 4.Edit Contact\n 5.Delete Contact\n 6.Exit\n Enter your choice "))
    if choice==1:
        name=input("Enter the Contact Name ")
        phone=input("enter the mobile Number ")
        contact[name]=phone
    elif choice==2:
        search_name=input("enter the contact name ")
        if search_name in contact:
            print(search_name,"'s contact number is",contact[search_name])
        else:
            print("Name is not found in Contact book")
    elif choice==3:
        if not contact:
            print("empty contact book")
        else:
            display_contact()
    elif choice==4:
        edit_contact=input("Enter the Contact to be edited")
        if edit_contact in contact:
            phone=input("enter Mobile Number")
            contact[edit_contact]=phone
            print("contact updated")
            display_contact()
        else:
            print("Name is not found in Contact book")
    elif choice==5:
        del_contact=input("Enter the contact to be Deleted")
        if del_contact in contact:
            confirm=input("Do you want to Delete this contact y/n?")
            if confirm=='y' or confirm=='y':
                contact.pop(del_contact)
            display_contact()
        else:
            print("Name is not found in the contact book")
    else:
        break
