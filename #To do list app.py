#to do list app
print('Welcome to My To-Do List')
task =[]
while True:
    x=input('Do you want to add a task(Yes/No) :')
    if x=='Yes':
        y=input('Enter your task:')
        task.append(y)
        y = ' '.join(task)
        print('====== YOUR TASKS ======')
        print('-',y)
    else:
        g = input('Do you want to remove a task(Yes/No):')
        if g=='Yes':
            h=input('What task do you want to remove: ')
            if h in task:
                task.remove(h)
                print('====== YOUR TASKS ======')
                y = ' '.join(task)
                print(y)
            else :
                print('This task is not present in you list')
        else:
            print('====== YOUR TASKS ======')
            y = ' '.join(task)
            print(y)
    b = input('Do you want to exit(Yes/No):')
    if b=='Yes':
        break
