# -*- coding: utf-8 -*-

""" 
@File name: Exercise_3_5_Vikas_singh.py
@Author: Vikas Singh
@description: Three dice roll

"""

import random


class Dice(object):
    dice_id_count = 1

    def __init__(self,dice_color):
        self.__side = 1
        self.__color = dice_color
        self.__id = Dice.dice_id_count
        Dice.dice_id_count += 1

    def roll_dice(self,dice_side):
        self.__side = dice_side

    def get_dice_side(self):
        return self.__side    

    def get_dice_color(self):
        return self.__color
    
    def set_color(self, dice_color):
        self.__color = dice_color

    def get_id(self):
        return self.__id

def roll_dices(dice_list):
    
    new_dice_list = []
    for i in dice_list:
        my_dice_numb = random.randint(1,6)
        i.roll_dice(my_dice_numb)
        new_dice_list.append(i)
    
    return new_dice_list
        

def make_list():

    dice_list = []

    for number in range(1, 4):
        print('For Dice ', number)
        color = input('Enter color: ')

        my_dice = Dice(color)

        dice_list.append(my_dice)

    return dice_list

def current_state_dice(dice_list):    
    print('Dice id :', dice_list.get_id(),'\nDice color :',dice_list.get_dice_color(),'\nDice sideup :',dice_list.get_dice_side())

def current_state_dices(dice_list):

    for i in dice_list:
        print('\nDice id :', i.get_id(),'\nDice color :',i.get_dice_color(),'\nDice sideup :',i.get_dice_side())

def check(tied_dice_list,dice1,dice2):
    if not tied_dice_list:
        tied_dice_list.append(dice1)
        tied_dice_list.append(dice2)
    else:
        for i in tied_dice_list:
            
            if int(i.get_id()) == int(dice1.get_id()):
                pass
                
            else:            
                tied_dice_list.append(dice1)
                

            if int(i.get_id()) == int(dice2.get_id()):
                pass
            else:
                tied_dice_list.append(dice2)
                
    

    return tied_dice_list

def tied_rematch(tied_dice_list):

    print('\nOOPs! there was a tie.')
    print('The tied dices are...')
    current_state_dices(tied_dice_list)
    print('\nRematch of the tied dices..')
    print('\nRolling dices.')
    new_tied_match = roll_dices(tied_dice_list)




def tied_check(dice_list):
    tied_dice_list = [] 

    while True:
        if 
        for i in range(0,len(dice_list)):
                    
        for j in range(i+1, len(dice_list)):
            if int(dice_list[i].get_dice_side()) == int(dice_list[j].get_dice_side()):
                tied_dice_list = check(tied_dice_list,dice_list[i],dice_list[j])                
    tied_rematch(tied_dice_list)








def main():
    # Ask the user to input the colors of the dice and make a list
    dice_list = make_list()

    # current state of the dices
    print('Current status of the dices is....') 
    current_state_dices(dice_list)

    #
    print('\n\n############ 1st ROUND ############\n\n')
    print('Rolling the dices...')
    dice_list = roll_dices(dice_list)
    print('\nCurrent status of the dices is....\n') 
    current_state_dices(dice_list)

    tied_check(dice_list)



    

    #


main()