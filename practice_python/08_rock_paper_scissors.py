


# while True:
#     print ("Welcome to Rock - Paper - Scissors Game!")
#     player1 = input("Enter the first player's name :")
#     player2 = input("Enter the second player's name :")

#     choice1 = input(f"{player1} Rock - Paper - Scissors :")
#     choice2 = input(f"{player2} Rock - Paper - Scissors :")
#     choice1.lower()
#     choice2.lower()
#     if choice1 == choice2:
#         print (f"It is tie!")

#     elif choice1 == 'rock' :
#         if choice2 == 'scrissors':
#             print (f"{player1} wins! Good Joob !")
#         else: print (f"{player2} wins! Good Job!")

#     elif choice1 == 'scissors' :
#         if choice2 == 'paper':
#             print (f"{player1} wins! Good Joob !")
#         else: print (f"{player2} wins! Good Job!")

#     elif choice1 == 'paper' :
#         if choice2 == 'rock':
#             print (f"{player1} wins! Good Joob !")
#         else: print (f"{player2} wins! Good Job!")

#     else:
#         print("You must enter rock,paper or scissors. :/")

    

#     answer = input('Do you want to start a new game? (Yes or No) :')
    
#     if answer == 'yes':
#         print('New game will start')
#     elif answer == 'no':
#         print('GAME OVER')
#         break
#     else:
#         print("Wrong answer, please enter 'yes' or 'no'!")

    
import random
#Extras
print ("Welcome to Rock - Paper - Scissors Game!")
while True:
    rps = ["rock","paper","scissors"]

    computer_choice = random.choice(rps)
    
    player_choice = input("Rock - Paper - Scissors :")
    player_choice.lower()

    if player_choice == computer_choice:
        print (f"It is tie!")

    elif player_choice == 'rock' :
        if computer_choice == 'scrissors':
            print (f"Player wins! Good Joob !")
        else: print (f"Computer wins!")

    elif player_choice == 'scissors' :
        if computer_choice == 'paper':
            print (f"Player wins! Good Joob !")
        else: print (f"Computer wins!")

    elif player_choice == 'paper' :
        if computer_choice == 'rock':
            print (f"Player wins! Good Joob !")
        else: print (f"Computer wins!")

    else:
        print("You must enter rock,paper or scissors. :/")

    
    
    answer = input('Do you want to start a new game? (Yes or No) :')
    
    if answer == 'yes':
        print('New game will start')
    elif answer == 'no':
        print('GAME OVER')
        break
    else:
        print("Wrong answer, please enter 'yes' or 'no'!")
        




        

        
    
    