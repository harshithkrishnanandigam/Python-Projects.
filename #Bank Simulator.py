#Bank Simulator
print("==================================\nWelcome to the Bank Simulator\n==================================")
x = int(input("Enter your PIN: "))
balance = 1000
history = []
y = input('Please select an option:\n1. Check Balance\n2. Deposit Money\n3. Withdraw Money\n4. Change Pin\n5. Transaction History\n6. Exit\n')
while True:
    if y == '1':
          print(f"Your balance is: ${balance}")
    elif y == '2':
        deposit = int(input("Enter the amount to deposit: "))
        balance = balance + deposit
        print(f"You have deposited ${deposit}. Your new balance is: ${balance}")
        history.append(f'deposit: ${deposit}')
    elif y == '3':
        withdraw = int(input("Enter the amount to withdraw: "))
        if withdraw > balance:
            print("Insufficient funds. Your current balance is: ${}".format(balance))
        else:
            balance = balance - withdraw
            print(f"You have withdrawn ${withdraw}. Your new balance is: ${balance}")
    elif y == '4':
        z = int(input("Enter your PIN: "))
        if z==x:
            n = int(input('Enter your new PIN:'))
            x = n
            print('PIN changed succesfully')
        else:
            print('Your PIN is incorrect. Please try again')
    elif y == '5':
        a = " ".join(history)
        print(a)
    elif y == '6':
        print("Thank you for using the Bank Simulator. Goodbye!")
        break