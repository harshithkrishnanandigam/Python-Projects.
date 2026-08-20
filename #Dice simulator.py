##Dice simulator
import random
print('Welcome to the dice simulator!!')
def single_dice():
    while True:
        x = input('Do you want to roll the dice?(yes/no) ')
        x = x.lower()
        if x== 'yes':
            a = random.randint(1,6)
            print(a)
            
        elif x == 'no':
            print('Thanks for playing!')
            break
        else:
            print('Please enter a valid response')

def double_dice():
    while True:
            x = input('Do you want to roll the dice?(yes/no) ')
            x = x.lower()
            if x== 'yes':
                dice1 = random.randint(1,6)
                dice2 = random.randint(1,6)
                print(dice1)
                print(dice2)
                print('Total',dice1+dice2)
                
            elif x == 'no':
                print('Thanks for playing!')
                break
            else:
                print('Please enter a valid response')

y = input('Do you want to choose a single dice or double dice(1/2): ')
if y =='1':
    single_dice()
elif y =='2':
    double_dice()
else:
    print('Siggundha ra puka, enni sarlu dengali ra ninnu attar lanja, manishive na ra puka, cheppindhi chey ra lanja munda')