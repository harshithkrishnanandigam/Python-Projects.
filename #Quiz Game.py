#Quiz Game
questions = ('1. What is the capital of Australia?',
             '2. Which planet is known as the Red Planet?',
             '3. What is the largest ocean on Earth?',
             '4. Which language is primarily used to create the structure of web pages?',
             '5. What is the chemical symbol for gold?')
options = (('A. Sydney','B. Melbourne','C. Canberra','D. Perth'),
           ('A. Venus', 'B. Mars','C. Jupiter' ,'D. Mercury'),
           ("A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"),
           ("A. Python", "B. HTML", "C. C++", "D. SQL"),
           ("A. Ag", "B. Gd", "C. Au", "D. Go"))
answers = ['C','B','D','B','C']
score = 0
question_number = 0
for question in questions:
    print(question)
    for option in options[question_number]:
        print(option)
    x = input('Enter your answer(A/B/C/D): ')
    if x == answers[question_number]:
        score+=1
        print('Your answer is correct')
        print(f'Your score is {score}')
    else:
        print('The answer is incorrect')
        print(f"The coorect answer is{options[question_number]}")
        print(f'Your score is {score}')
    question_number+=1
print(f'Your efficiency is {(score//len(answers))*100}')