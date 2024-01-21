rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
if int(user_choice) >= 3 or int(user_choice) < 0:
    print("Sorry that was not a choice. Game over")
else:
        
    choices = [rock, paper, scissors]

    print(choices[int(user_choice)])
    print(f"\nComputer chose:\n")

    computer_choice = random.randint(0, 2)
    print(choices[int(computer_choice)])
    # print(computer_choice)

    if int(user_choice) == int(computer_choice):
        print("It is a tie")
    elif int(user_choice) == 0 and int(computer_choice) == 1:
        print("You lose")
    elif int(user_choice) == 0 and int(computer_choice) == 2:
        print("You win")
    elif int(user_choice) == 1 and int(computer_choice) == 0:
        print("You win")
    elif int(user_choice) == 1 and int(computer_choice) == 2:
        print("You lose")
