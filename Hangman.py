##Hangman
import random
list = ['password','generator','python','project','explorer','file','edit','selection','view']
ran = random.choice(list)
x = input('enter your guess: ')
print('_'*len(ran))
life = 0
# three lifes
if x.lower() in ran:
    print('your choice is correct')
    for i in range(0,len(ran)):
        if ran[i]!=x:
            print('_')
        elif ran[i]==x:
            print(ran[i])
else:
    life+=1
    print('your choice is incorrect')