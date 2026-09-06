#Password generator

import random

print('============= PASSWORD GENERATOR ================')

print('Password types available:')
print('1. Small letters only')
print('2. Capital letters only')
print('3. Numbers only')
print('4. Special characters only')
print('5. Mixed (small, capital, numbers, special characters)')

choice = input('Enter the number corresponding to your choice: ')
    
if choice == '1':
        x = int(input('Enter your password length:'))
        def password_generator(x):
            small_letters = 'abcdefghijklmnopqrstuvwxyz'
            p = []
            for i in range(x):
                pas = random.choice(small_letters)
                p.append(pas)
            return ''.join(p)
        print(password_generator(x))
    
elif choice == '2':
        x = int(input('Enter your password length:'))
        def password_generator(x):
            capital_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            p = []
            for i in range(x):
                pas = random.choice(capital_letters)
                p.append(pas)
            return ''.join(p)
        print(password_generator(x))
        
elif choice == '3':
        x = int(input('Enter your password length:'))
        def password_generator(x):
            numbers = '1234567890'
            p = []
            for i in range(x):
                pas = random.choice(numbers)
                p.append(pas)
            return ''.join(p)
        print(password_generator(x))
        
elif choice == '4':
        x = int(input('Enter your password length:'))
        def password_generator(x):
            special_characters = '!@#$%^&*()_+=`~<>?:"}{|,./;[]`'
            p = []
            for i in range(x):
                pas = random.choice(special_characters)
                p.append(pas)
            return ''.join(p)
        print(password_generator(x))
        
elif choice == '5':
        x = int(input('Enter your password length:'))
        def password_generator(x):
            mixed_characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+=`~<>?:"}{|,./;[]`'
            p = []
            for i in range(x):
                pas = random.choice(mixed_characters)
                p.append(pas)
            return ''.join(p)
        print(password_generator(x))
