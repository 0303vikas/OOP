import random

# Game class contain the randomly selected 10 countries for quiz
# Calls class Country and starts the game
class Game(object):

    # method contains the initial state of the function
    def __init__(self,dictionary):        
        self.dictionary = dictionary        

    # method calls a for loop, which will be repeated for every element in dictionary
    def get_country(self):
        for i in range(0,len(self.dictionary)):
            # class Country is initalized, and 3 arguments are given id of the question(used for numbering the questions),
            # country of the dictionary element, capital of the dictionary element
            game = Country(i+1,self.dictionary[i][0],self.dictionary[i][1])

# Class Country hold individual country and its capital city
# calculated the score of the game
class Country(object):
    # variable for keeping the score count
    score = 0
    # method to keep the initial state of the class
    def __init__(self,ID,country,capital):
        self.id = ID
        self.country = country
        self.capital = capital
        self.game_play()
    # method game_play keeps starts the game and adds 1 point to the final score for each correct answer
    def game_play(self):
        
        print("Question ",self.id,". What is the capital of ",self.country,": ")
        # ask for user answer
        input_user = input('User Answer: ')

        # converts the user answer and correct answer to capital to compare them
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

# main function
def main():
    # dictionary keeps all the country and their capital city
    dictionary = {}

    # try to open the file to read all the country and their capital
    try:
        filek = open("capital.txt", "r")             
    except:
        print("Sorry the file cann't be opened")

    # read the text file line wise and puts the country and capital as single list element
    # remove the comman between the list item and seperate the capital and country into a new list as sepearte list item
    # then putting the county as key and capital as values into the dictionary
    for i in filek:
        line_capital_city = filek.readline().splitlines()       
        line_capital_city_seperate = line_capital_city[0].split(',')        
        
        countname = line_capital_city_seperate[0]
        capitalname = line_capital_city_seperate[1]                  
        dictionary[countname] = capitalname
    # printing dictionary
    print(dictionary)

    # selection of 10 random countries from the dictionary and passing them to class Game
    settinggame = Game(random.sample(dictionary.items(),10))  
    # game begins by calling method get_county of the class Game
    print("game begins")
    settinggame.get_country()

main()