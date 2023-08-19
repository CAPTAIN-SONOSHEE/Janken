import random
janken = ['''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
, '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''', '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''']

computer_choice = random.randint(0,2)

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
else:  
    print(janken[user_choice]+"\n")
    print("Computer chose:\n")
    print(janken[computer_choice]+"\n")


    if (computer_choice > user_choice) or (user_choice == 2 and computer_choice == 0) :
        print("You lose")
    elif user_choice == computer_choice:
        print("Draw")
    else:
     print("You win")
