# File:  Exercise8_5_Vikas_singh.py
# Author: Vikas Singh       
# Description:  extension of country/capital quiz

import random

# Game class contain the randomly selected 10 countries for quiz
# Calls class Country and starts the game
class Game(object):

    # method contains the initial state of the function
    def __init__(self,dictionary,game_choice):        
        self.dictionary = dictionary
        self.game_choice = game_choice        

    # method calls a for loop, which will be repeated for every element in dictionary
    def get_country(self):
        for i in range(0,len(self.dictionary)):
            # class Country is initalized, and 3 arguments are given id of the question(used for numbering the questions),
            # country of the dictionary element, capital of the dictionary element
            Country(i+1,self.dictionary[i][0],self.dictionary[i][1],self.game_choice)

# Class Country hold individual country and its capital city
# calculated the score of the game
class Country(object):
    # variable for keeping the score count
    score = 0
    # method to keep the initial state of the class
    def __init__(self,ID,country,capital,game_choice):
        self.id = ID
        self.country = country
        self.capital = capital
        self.game_play(game_choice)

    # method game_play keeps starts the game and adds 1 point to the final score for each correct answer
    def game_play(self,game_choice):
        
        # here depend on the user choice(either 1 or 2) one game is selected according to user input
        # if 1 is entered by the user then guess the country is played
        # elif 2 is entered by the user, then guess the capital city is played
        if game_choice == 1:
            print("\nGuess the capital of the country...\n")
            print("Question ",self.id,". What is the capital of ",self.country,": ")
            # ask for user answer
            input_user = input('User Answer: ')

            # converts the user answer and correct answer to capital letters to compare them
            if input_user.upper()== self.capital.upper():
                print("Correct Answer.")
                print('You get 1 point.\n')
                # increment the score by 1 if the answer is correct
                Country.score += 1
                # print the result if the id of the question is 10
                if self.id == 10:
                    print("\nGame Finished.\nThe Final score is",Country.score," out of 10")           
            else:
                print("Wrong answer")
                print('Correct answer is ', self.capital,'\n')            
                if self.id == 10:
                    print("\nGame Finished.\nThe Final score is",Country.score," out of 10")            
        elif game_choice == 2:
            print("\nGuess the country from the capital...\n")
            print("Question ",self.id,". Which countries capital is ",self.capital,": ")
            # ask for user answer
            input_user = input('User Answer: ')

            # converts the user answer and correct answer to capital letters to compare them
            if input_user.upper()== self.country.upper():
                print("Correct Answer.")
                print('You get 1 point.\n')
                # increment the score by 1 if the answer is correct
                Country.score += 1
                # print the result if the id of the question is 10
                if self.id == 10:
                    print("\nGame Finished.\nThe Final score is",Country.score," out of 10")           
            else:
                print("Wrong answer")
                print('Correct answer is ', self.country,'\n')            
                if self.id == 10:
                    print("\nGame Finished.\nThe Final score is",Country.score," out of 10")     
       

# main function
def main():

    # dictionary keeps all the country and their capital city
    dictionary = {}

    # try to open the file to read all the country and their capital
    try:        
        hellohello = open("capital.txt", "r")
                    
    except:
        print("Sorry the file cann't be opened")

    # read the text file line wise and puts the country and capital as single list element
    # remove the comman between the list item and seperate the capital and country into a new list as sepearte list item
    # then putting the county as key and capital as values into the dictionary
    for i in hellohello:
        line_capital_city = hellohello.readline().splitlines()       
        line_capital_city_seperate = line_capital_city[0].split(',')        
        
        countname = line_capital_city_seperate[0]
        capitalname = line_capital_city_seperate[1]                  
        dictionary[countname] = capitalname
    # printing dictionary
    print(dictionary)

    # Ask user, which type of game they want to play
    # option 1 is guess the capital's name from country name
    # option 2 is guess the country's name from capital city
    print('')
    user_game_choice = int(input("Choose your option, enter 1 or 2...\nPress 1 if you want to guess capital name from country name\nPress 2 if you want to guess country name from capital name.\nYour choice: "))
    

    # selection of 10 random countries from the dictionary and passing them to class Game
    # alse user input either 1 or 2 is given while creating an instance of the class
    settinggame = Game(random.sample(dictionary.items(),10),user_game_choice)  
    # game begins by calling method get_county of the class Game
   
    print("\n###### Game begins ######")

    
    settinggame.get_country()

main()