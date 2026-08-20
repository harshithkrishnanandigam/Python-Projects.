#Expense Tracker
print("=========== EXPENSE TRACKER =============")
print('1. Add expense\n 2. View expenses\n3. Show total spending\n4. Search\n5. Delete an expense\n6. Exit')

expenses = []


def Printing():
    print('================= YOUR EXPENSES =================')
    print('AMOUNT     CATEGORY       DESCRIPTION')
    

    for expense in expenses:
        print(expense[0], '\t\t', expense[1], '\t\t', expense[2])
    return


def Search():
            
            found_expenses = []

            
            for exp in found_expenses:
                    print(exp[0], '\t\t', exp[1], '\t\t', exp[2])
                    for exp in found_expenses:
                         print('AMOUNT     CATEGORY       DESCRIPTION')
                         print(exp[0], '\t\t', exp[1], '\t\t', exp[2])
            return
                

def remove():
                search_name = input('Enter the category you want to remove: ')
                found_expenses = []
                for expense in expenses:
                    if expense[1].lower() == search_name.lower():
                        expenses.remove(expense)
                        return
                    if len(found_expenses) == 0:
                         print('Expense not found!')
                

while True:
    a = input('Enter your choice(1,2,3,4,5,6): ')
    if a=='1':
        x = int(input('Enter the amount you have spent: '))
        y = input('Name the category in which you have spent: ')
        z = input('Describe the category in which  you have spent: ')
        expenses.append([x, y, z])
        print('Expense added successfully')
        Printing()
    elif a=='2':
        Printing()
    elif a =='3':
        total = 0
        for expense in expenses:
            total+=(expense[0])
        print('Your total spending is',total)
    elif a =='4':
        Search()
    elif a =='5':
        remove()
    elif a =='6':
        break
    else:
        print('Why are you dumb?\n bitch!!!!')