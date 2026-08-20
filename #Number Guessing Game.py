#Number Guessing Game
import random
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("You have 10 attempts to guess the number.")

def play_game():
    number = random.randint(1, 100)
    attempt = 0
    while attempt < 10:
        
        try:
            print(f"Attempt {attempt + 1}:")
            x = int(input("Please enter your guess: "))
        except:
            print("Please enter a valid number.")
            continue
        attempt += 1
        
        if x == number:
            print(f"your guess is correct\nyou have guessed the correct number in attempt number {attempt}")
            print("You have won the game!")
            y = input("Do you want to play again? (yes/no): ")
            if y.lower() == 'yes':
                play_game()
            else:
                print("Thank you for playing the Number Guessing Game!")
            break
        elif x < number:
                print("Your guess is too low.")
                print('Your guess is incorrect.\nplease try again')
        elif x > number:
            print("Your guess is too high.")
            print('Your guess is incorrect.\nplease try again')
        if attempt == 10:
            print(f"Sorry, you've used all your attempts. The correct number was {number}.")
            try:
                y = input("Do you want to play again? (yes/no): ")
                if y.lower() == 'yes':
                    play_game()
            except KeyboardInterrupt:
                print("Game interrupted. Thank you for playing the Number Guessing Game!")
play_game()