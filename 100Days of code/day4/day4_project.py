import random

computer_options = ['rock','paper','scissors']
user_input = input("Rock, Paper Scissors select")
computer = random.choice(computer_options)

user_lower = user_input.lower()
print(computer)
if computer == user_input:
    print("Draw")
elif computer =='rock' and user_lower == 'scissors':
    print('Computer Wins')
elif computer =='paper' and user_lower == 'rock':
    print('Computer Wins')
elif computer =='scissors' and user_lower == 'paper':
    print('Computer Wins')
elif user_input not in computer_options:
    print("Invalid option You lose")
else:
    print("You won")











