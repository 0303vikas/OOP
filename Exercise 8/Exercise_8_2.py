# -*- coding: utf-8 -*-

""" 
@File name: Exercise_8_2_Vikas_singh.py
@Author: Vikas Singh
@description: Implementing cookie state diagram

"""

import random
import time

# main class Cookies
class Cookies:
    # method init stores the date attributes for the class
    # date variables are cookies basket and cookies flavour
    def __init__(self,cookie_basket,flavour):
        self.__cookies_basket = cookie_basket
        self.__cookies_flavour = flavour 

    # set the cookie basket list
    def set_cookie_basket(self,cookie_basket):
        self.__cookies_basket = cookie_basket

    # return the cookies basket
    def get_cookie_basket(self):
        return self.__cookies_basket

    # set flavour, flavour input is taken from user in main function
    def set_flavour(self,flavour):
        self.__cookies_flavour = flavour
    
    # frosting flavour picks a random frosting flavour, from all the 
    # flavour present in the list
    def frosting_flavour(self):
        flavour_list = ["Blueberry","strawberry","mango","chocolate","raspberry"]
        self.__cookies_flavour = random.choice(flavour_list)        

    # gets the flavour of the cookies        
    def get_flavour(self):
        return self.__cookies_flavour
    
    # prints the current state of the class    
    def __str__(self):
        return "\nHere are your " + str(len(self.__cookies_basket)) + " cookies.\n Flavour of the cookies is :" + str(self.__cookies_flavour)



# main function
def main():
    # make object/instance of Cookie class
    # for start we choose random flavour for the cookies
    set_cookie_list= Cookies("","")
    print("Choosing a flavour....")    
    set_cookie_list.frosting_flavour()
    print("The flavour is :", set_cookie_list.get_flavour())
    
   
    # while loop will continue asking flavour from the user, and
    # will bake the cookies one by one and them add frosting one by one
    # again aske user if current flavour is correct/favourite untill user says yes
    while True:

        print("It take's 2 second to bake one cookie\n")
        print('Starting baking cookies...\n')

        # store all cookies
        cookies_basket = []

        # create 10 cookies one by one
        # sleep time is set to show the time taken to bake one cookie
        # sleept time will delay the execution of the code by the time specified in it
        for i in range(1,11):
            print("\nCookie in oven...")
            time.sleep(2)
            print("Cookie ",i," ready.")
            cookies_basket.append(i)    
        
        # send cookie basket to cookies class
        set_cookie_list.set_cookie_basket(cookies_basket)
    
        print("\nAll cookies baked.")
        print('\nFrosting process begins')
        print('\nFrosting a cookie takes one second.')

        # get cookies basket from class for frosting
        cookies_basket = set_cookie_list.get_cookie_basket()

        # add frosting to each cookie one by one
        # it takes 1 second time to add frosting to a cookie
        for i in cookies_basket:
            print('\nAdding frosting to cookie...')
        
            time.sleep(1)
            print("Cookie",i," ready.")
        
        # print the order
        print("\nOrder ready....")
        print(set_cookie_list)

        print('')
        print("Is this your favourite flavour?")

        # ask user if the flavour is their favourite flavour 
        user_choice = int(input("Press 1 for yes and press 2 for no: "))

        # if user choice is 1, give user the order and break the while loop
        # elif user choice is 2, then ask user to choose their favourite flavour
        # from the user and make cookies of that flavour again
        if user_choice == 1:
            print('Thank you, enjoy your food.')
            break
        elif user_choice == 2:
            print('Sorry, which flavour do you want?')
            print("\nPress 1 for Blueberry flavour")
            print("Press 2 for Strawberry flavour")
            print("Press 3 for mango flavour")
            print("Press 4 for chocolate flavour")
            print("Press 5 for raspberry flavour")
            user_flavour = int(input("Your choice: "))
            if user_flavour == 1:
                set_cookie_list.set_flavour("Blueberry")
            elif user_flavour ==2:
                set_cookie_list.set_flavour("Strawberry")
            elif user_flavour == 3:
                set_cookie_list.set_flavour("Mango")
            elif user_flavour == 4:
                set_cookie_list.set_flavour("Chocolate")
            elif user_flavour == 5:
                set_cookie_list.set_flavour("Raspberry")
            continue

# running the main function
main()

    
    

    

     








    



    

    





main()