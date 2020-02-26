#rock.py
#2-24-2020
#Aman Pruthi

import random
while True:
    #Provide options
    options = ["Rock","Paper","Scissors"]
    AI = random.choice(options)

    #Input for the user
    user = input("Pick either Rock, Paper or Scissors: ")

    #As the AI has its first letter capital, we have to make it small.
    user = user.lower()

    #Defining Scenarios
    print ('AI chose - ', AI)
    if user == 'rock':
        if AI == 'Rock':
            print ('Tie Game')
        elif AI == 'Paper':
            print ('AI Wins')
        else:
            print ('User Wins')
    elif user == 'paper':
        if AI == 'Rock':
            print ('User Wins')
        elif AI == 'Paper':
            print ('Tie Game')
        else:
            print ('AI Wins')
    elif user == 'scissors':
        if AI == 'Rock':
            print ('AI Wins')
        elif AI == 'Paper':
            print ('User Wins')
        else:
            print ('Tie Game')
    else:
        print ('Error! Check your spellings.')
    Again = input("Do you want to play again? (Y/N)")
    if Again == "N":
        break

