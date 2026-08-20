
import random
small_letters = 'abcdefghijklmnopqrstuvwxyz'
capital_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
characters = '!@#$%^&*()_+=`~<>?:"}{|,./;[]\`'
numbers = '1234567890'
sl = list(small_letters)
cl = list(capital_letters)
ch = list(characters)
n = list(numbers)
def password_generator():
    try:
        x = int(input('Enter the length of the password:'))
    except ValueError:
        print('Please enter a valid integer for the password length.') 
    dec = 0
    if x%2 == 0:
        a = x/4
    else:
        a = x//4
        dec = 1
    slist = []
    a = x//4
    while a>0:
        schoosing= random.choice(sl)
        a = a-1
        slist.append(schoosing)
    clist = []
    a = x//4
    while a>0:
        cchoosing= random.choice(cl)
        a = a-1
        clist.append(cchoosing)
    chlist = []
    a = x//4
    while a>0:
        chchoosing= random.choice(ch)
        a = a-1
        chlist.append(chchoosing)
    nlist = []
    a = x//4
    while a>0:
        nchoosing= random.choice(n)
        a = a-1
        nlist.append(nchoosing)
    password_list = slist+clist+nlist+chlist
    if dec == 1:
        f = random.choice(password_list)
        password_list.append(f)
    random.shuffle(password_list)
    b = ''.join(password_list)
    print(len(b), b)
    return b
password_generator()