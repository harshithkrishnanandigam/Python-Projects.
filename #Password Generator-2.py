import random

x = int(input('Enter your password length:'))
def password_generator(x):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=`~<>?:"}{|,./;[]`1234567890'
    p = []
    for i in range(x):
        pas = random.choice(characters)
        p.append(pas)
    return ''.join(p)

print(password_generator(x))