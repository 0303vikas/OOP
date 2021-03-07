# -*- coding: utf-8 -*-

"""

@File name: Exercise_4_7_Vikas_singh.py
@Author: Vikas singh
@description: Making mammal object

"""

import random

class Dice:
    def __init__(self):
        self.side = '' # store the side number        

    # function to roll in unbaised dice
    def roll_dice(self):
        dice_face = random.randint(1,6) 
        self.side = dice_face   
   
    # function to return the side 
    def get_dice_side(self):
        return self.side
   
    # function to print the current state of the class.
    def __str__(self):
        return f"""SideUp :{self.side}"""



class Mammal(object):

    mammal_count = 1
    def __init__(self,Species,name,size,weight,dimension):
        self.__id = Mammal.mammal_count
        self.__species = Species
        self.__name = name
        self.__size = size
        self.__weight = weight
        self.__dimension = dimension
        Mammal.mammal_count += 1

    def get_dimension(self):
        return self.__dimension

    def __str__(self):
        return f"""ID :{self.__id}\nSpecies :{self.__species}\nName :{self.__name}\nSize in meters :{self.__size}\nWeight in kg :{self.__weight}\nDimension in m square :{self.__dimension}"""

class Car:

    def __init__(self,manu,mod,mil,pri,col,maxl,siz):
        self.__manufacturer = manu
        self.__model = mod
        self.__mileage = mil
        self.__price = pri
        self.__color = col
        self.__maxloadlimit = maxl
        self.__sizeoftruck = siz

    # function to set the name of the manufacturer
    def set_manu(self,manufacturer):
        self.__manufacturer = manufacturer
    # function to set the name of the model
    def set_mod(self, model):
        self.__model = model
    # function to set the mileage of the car
    def set_mil(self, mileage):
        self.__mileage = mileage
    # function to set the price of the car
    def set_pri(self, price):
        self.__price = price
     # function to set the color of the car
    def set_col(self, color):
        self.__color = color
    # function to set the maxload of the car
    def set_maxl(self, maxloadsize):
        self.__maxloadlimit = maxloadsize
    # function to set the size of the car
    def set_siz(self, size):
        self.__sizeoftruck = size
    # function to get the manufacturer of the car
    def get_manu(self):
        return self.__manufacturer
    # function to get the model of the car
    def get_mod(self):
        return self.__model
    # function to get the mileage of the car
    def get_mil(self):
        return self.__mileage
    # function to get the price of the car
    def get_pri(self):
        return self.__price
    # function to get the color of the car
    def get_col(self):
        return self.__color
    # function to get the maxload of the car
    def get_maxl(self):
        return self.__maxloadlimit
    # function to get the size of the car
    def get_siz(self):
        return self.__sizeoftruck

    # function to print the state of the class        
    def __str__(self):
        return f"""Manufacturer :{self.__manufacturer}\nModel :{self.__model}\nMileage :{self.__mileage}\nPrice :{self.__price}\nColor :{self.__color}\nMaxLoadLimit :{self.__maxloadlimit}\nSizeofTruck :{self.__sizeoftruck}"""


def main():
    # inputs to get the user input for the car details
    manufacturer = input('Name of the car manufacturer :')
    model = input('Model of the car :')
    mileage = input('Mileage of the car :')
    price = input('Price of the car :')
    color = input('Color of the car :')
    maxload = input('Maxload of the car should be > 400kg:')
    maxsize = input('Maxsize of the car in in square meter:')

    # init the class car and set the car details
    call_car = Car(manufacturer, model, mileage, price, color,maxload,maxsize)
    print('Here is the car details entered by the user.')

    # print the car details provided by the user
    print(call_car)

    global mammal1 
    mammal1 = Mammal('Bear','Brown Bear','3','250','4.5')
    global mammal2 
    mammal2 = Mammal('Wolf','Arctic wolf','1.5','50','1.2')
    global mammal3 
    mammal3 = Mammal('Cat','Indian Tiger','3','220','3')
    global mammal4 
    mammal4 = Mammal('Cat','Lion','2','190','2.4')
    global mammal5 
    mammal5 = Mammal('Elephant','Elephant','6','400','16.8')
    global mammal6 
    mammal6 = Mammal('Monkey','India monkey','0.5','7.7','0.25')

    print('Now rolling the dice.')
    # initialize the class dice
    roll_dice = Dice()

    roll_dice.roll_dice()
    print(roll_dice)

    print('The select animal is..')

    number = str(roll_dice.side)
    mammal_var = 'mammal'
    print(globals()[mammal_var + str(number)])    

    dimensionofcar = globals()[mammal_var + str(number)].get_dimension()
    
    
    print("Dimension of car is ",call_car.get_siz(),'square meter.')
    if float(dimensionofcar) > float(call_car.get_siz()):
        print('Sorry, the animal cannot fit in your car.')
    else:
        print('The animal can fit in the car, have a safe trip.')
    

    print(call_car.get_siz())


    

main()








    

