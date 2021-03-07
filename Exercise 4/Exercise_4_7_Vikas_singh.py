# -*- coding: utf-8 -*-

"""

@File name: Exercise_4_7_Vikas_singh.py
@Author: Vikas singh
@description: Making car object

"""

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
        return f"""Manufacturer :{self.__manufacturer}
                   Model :{self.__model}\nMileage :{self.__mileage}\nPrice :{self.__price}\nColor :{self.__color}\nMaxLoadLimit :{self.__maxloadlimit}\nSizeofTruck :{self.__sizeoftruck}"""


def main():

    # inputs to get the user input for the car details
    manufacturer = input('Name of the car manufacturer :')
    model = input('Model of the car :')
    mileage = input('Mileage of the car :')
    price = input('Price of the car :')
    color = input('Color of the car :')
    maxload = input('Maxload of the car :')
    maxsize = input('Maxsize of the car :')

    # init the class car and set the car details
    call_car = Car(manufacturer, model, mileage, price, color,maxload,maxsize)
    print('Here is the car details entered by the user.')

    # print the car details provided by the user
    print(call_car)

main()






    