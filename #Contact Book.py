contact_list = []

def Printing():
    print('================= YOUR CONTACTS =================')
    print('NAME     NUMBER       GMAIL')
    

    for contact in contact_list:
        print(contact[0], '\t\t', contact[1], '\t\t', contact[2])


def Search():
    search_name = input('Enter the name you want to search: ')

    for contact in contact_list:
        if contact[0].lower() == search_name.lower():
            print('Name:', contact[0])
            print('Number:', contact[1])
            print('Gmail:', contact[2])
            return
        else:
            print('Contact not found!')


while True:
    print('1. Add contact')
    print('2. Search contact')
    print('3. Show all contacts')
    print('4. Exit')

    choice = input('Enter your choice: ')

    if choice == '1':
        x = input('Enter the name: ')
        y = input('Enter the phone number: ')
        z = input('Enter the Gmail: ')

        contact_list.append([x, y, z])

    elif choice == '2':
        Search()

    elif choice == '3':
        Printing()

    elif choice == '4':
        print('Goodbye!')
        break

    else:
        print('Enter a valid choice!')