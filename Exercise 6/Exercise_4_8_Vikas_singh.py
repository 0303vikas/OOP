# -*- coding: utf-8 -*-

"""

@File name: Exercise_4_7_Vikas_singh.py
@Author: Vikas singh
@description: Making mammal object

"""

import random

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

    def __str__(self):    
        return f"""\nId : {self.__id}\nSpecies :{self.__species}\nName :{self.__name}\nSize in meters :{self.__size}\nWeight in kg :{self.__weight}\nDimension in m square :{self.__dimension}"""










    

