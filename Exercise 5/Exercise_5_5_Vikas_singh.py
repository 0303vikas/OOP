# -*- coding: utf-8 -*-

""" 
@File name: Exercise_3_5_Vikas_singh.py
@Author: Vikas Singh
@description: Making player dictionary

"""

import random

# main class player
class Player(object):
    id_count = 1 # keeps the count of player id 

    def __init__(self,fname,lname):
        self.__id = Player.id_count
        self.__firstname = fname
        self.__lastname = lname
        self.__diceside = 1
        Player.id_count += 1 # increment id for each new object created from class player

    #set the first name of the player
    def set_fname(self,fname):
        self.__firstname = fname
    
    #set the last name of the player
    def set_lname(self,lname):
        self.__lastname = lname
    
    #set the side of the dice
    def set_dice_side(self,side):
        self.__diceside = side
    
    #get the id of the dice 
    def get_id(self):
        return self.__id
    #get he first name of the player
    def get_fname(self):
        return self.__firstname
    #get the last name of the player
    def get_lname(self):
        return self.__lastname
    #get the side of the dice
    def get_diceside(self):
        return self.__diceside

    def __str__(self):
        return f"""Player_id: {self.__id}\nPlayer_first_name: {self.__firstname}\nPlayer_last_name: {self.__lastname}\nPlayer_side: {self.__diceside}"""

# function to make 4 different player
def make_player():
    # dictionary where all the information will be stored
    my_player_dict = {}

    # ask for 4 players name's from user
    # loop will run four times
    for i in range(1,5):
        print('For player', i)

        first_name = input('First Name :')
        second_name = input('Second Name :')
        #init the class Player and create 4 player objects when the loop gets over
        player_class = Player(first_name,second_name)
        # users player id as key and player object as values and put them in dictionary
        my_player_dict[player_class.get_id()] = player_class

    print('\n\nThe players participating are.....')
    # init show result function 
    # that shows the details of different players
    show_result(my_player_dict)
    return my_player_dict

#function to roll dice and change the values of the side for all the players
def roll_dice(player_dict):
    
    # run the function from 1 to the lenght of the players list 
    # generates random integer 
    for i in range(1,len(player_dict)+1):
        # generates random integer
        dice_roll = random.randint(1,6)
        #select the value of the key from the dictionary
        player_update = player_dict[i]
        # use the player class and update the side of the dice for each user
        player_update.set_dice_side(dice_roll)
        # update the entry in dictionary
        player_dict[i] = player_update

    return player_dict
# shown details of each player
def show_result(player_dict):

    for i in player_dict.values():
        print()        
        print(i)
        print()
        
# main function
def main():
    # init make player function
    player_dict = make_player()

    # initalize roll dice function
    print('\nRolling dices...\n')
    player_dict = roll_dice(player_dict)
    #initalzie show result function
    show_result(player_dict)

main()


    

