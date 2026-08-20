# Rock Paper Scissors Game
import random
print("Welcome to Rock Paper Scissors!")
print("In this game, you will play against the computer.\nYou will have 3 attempts to win the game.")
print("The rules are simple:\n- Rock beats Scissors\n- Scissors beats Paper\n- Paper beats Rock")

def playagain():
    y = input("Do you want to play again? (yes/no): ")
    if y.lower() == 'yes':
        play_game()
    else:
        print("Thank you for playing Rock Paper Scissors!")
    return

attempt = 0

def play_game():
    global attempt
    while attempt < 3:
        user_point = 0
        computer_point = 0
        list = ["r", "p", "s"]
        option = random.choice(list)
        attempt += 1
        print(f"Attempt {attempt}:")
        x = input("Enter your choice (rock(r), paper(p), scissors(s)): ").lower()
        def choosing():
            print("You chose", x)
            print("The computer chose", option)
            return
        if x == option:
            choosing()
            print("It's a tie! Both chose", option)
            continue
        elif x == 'r' and option == 's':
            user_point += 1
            choosing()
            print("You win! Rock beats scissors.")
            continue
        elif x == 'p' and option == 'r':
            user_point += 1
            choosing()
            print("You win! Paper beats rock.")
            continue
            
        elif x == 's' and option == 'p':
            user_point += 1
            choosing()
            print("You win! Scissors beats paper.")
            continue
        else:
            computer_point += 1
            choosing()
            print("You lose! The computer chose", option)
            continue
    return

play_game()