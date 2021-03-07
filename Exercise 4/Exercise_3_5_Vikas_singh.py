# -*- coding: utf-8 -*-

""" 
@File name: Exercise_3_5_Vikas_singh.py
@Author: Vikas Singh
@description: Making a dice roll program

"""

import random

class Dice:

    def __init__(self):
        self.side = '' # store the side number  
        self.color = '' # store the color

    # function to roll in unbaised dice
    def roll_dice(self):
        dice_face = random.randint(1,6) 
        self.side = dice_face
        # array that contains the set of all the color        
        color_collection = ['Yellow','Green','Red','violet','Orange','Indigo']
        self.color = color_collection[dice_face -1]
   
   
    # function to return the side 
    def get_dice_side(self):
        return self.side
    # function to return the color of the side
    def get_dice_color(self):
        return self.color
    # function to print the current state of the class.
    def __str__(self):
        return f"""SideUp :{self.side}\nColor :{self.color}"""

