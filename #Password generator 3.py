#Password generator
import random
small_letters = 'abcdefghijklmnopqrstuvwxyz'
capital_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
characters = '!@#$%^&*()_+=`~<>?:"}{|,./;[]`'
numbers = '1234567890'
sl = list(small_letters)
cl = list(capital_letters)
ch = list(characters)
n = list(numbers)

def password_generator():
    try:
        length = int(input('Enter the length of the password:'))
    except ValueError:
        print('Please enter a valid integer for the password length.') 
    slist = []
    clist = []
    chlist = []
    nlist = []
    
    while length>=4:
        schoosing= random.choice(sl)
        cchoosing= random.choice(cl)
        chchoosing= random.choice(ch)
        nchoosing= random.choice(n)
        length-=4
        slist.append(schoosing)
        clist.append(cchoosing)
        chlist.append(chchoosing)
        nlist.append(nchoosing)
        password_list = slist+clist+nlist+chlist
    while length>0:
        f = random.choice(password_list)
        password_list.append(f)
        length-=1

    random.shuffle(password_list)
    b = ''.join(password_list)
    return b

print(password_generator())
y = input('Do you want to save your password? (yes/no):')
while y == 'yes':
    password_generator()