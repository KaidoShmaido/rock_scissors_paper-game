import random
user_wins =  0
computer_wins = 0
options = ['rock','paper','scissors']
while True :
    user_choice = input('Type Rock/Paper/Scissors or Q to quit. ').lower()
    if user_choice == "q":
        break
    if user_choice not in options:
        continue
    
    
    random_number=random.randint(0, 2)
    #rock: 0 ,paper: 1 , scissors: 2 
    computer_guess = options[random_number]
    print("computer picked" ,computer_guess+ '.')
    
    if user_choice == "rock" and computer_guess=="scissors":
        print('you won! ')
        user_wins+=1
        
    
    elif user_choice == "paper" and computer_guess=="rock":
        print('you won! ')
        user_wins+=1
        
    
    elif user_choice == "scissors" and computer_guess=="paper":
        print('you won! ')
        user_wins+=1
    
    elif user_choice == computer_guess :
        print(' you are equal ')
        
    else:
        print('computer won !')
        computer_wins+=1

print("the computer won ",computer_wins,"times")
print("the user won ",user_wins,"times")

print('goodbye and thanks for playing ! ')
        
    