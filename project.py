#!/usr/bin/python3# Rock-Paper-Scissors Game
def get_user_choice():
    choice = input("Enter your choice (rock, paper, scissors): ")
    choice = choice.lower()  # Convert to lowercase for uniformity
    if choice == 'rock' or choice == 'paper' or choice == 'scissors':
        return choice
    else:
        print("Invalid choice! Please enter rock, paper, or scissors.")
        return get_user_choice()  # Recursive call for correct input

def get_computer_choice():
    import random
    options = ['rock', 'paper', 'scissors']
    comp_choice = random.choice(options)
    return comp_choice

def decide_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print("Computer chose:", computer_choice)
    result = decide_winner(user_choice, computer_choice)
    print(result)
main()




