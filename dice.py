#MODUL Dice
#write a function that will generate a number between 1 and 6

import random
print(random.randint(0,6))

#or this way:
#Import randint function
from random import randint

#define module#



#define function
def doubledice():
    dice1 = dice_roll()
    #roll 1 dice set as variable
    #roll 2nd dice set as variable
    dice2 = dice_roll()
    return f"Dice 1: {dice1}\nDice 2: {dice2}\nTotal: {dice1+dice2}"
    #returns ad dices 1 and 1 added together