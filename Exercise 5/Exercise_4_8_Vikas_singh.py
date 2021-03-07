# -*- coding: utf-8 -*-

"""

@File name: Exercise_4_7_Vikas_singh.py
@Author: Vikas singh
@description: Making mammal object

"""

import random

class Mammal():
    
    def __init__(self,Species,name,size,weight,dimension):        
        self.__species = Species
        self.__name = name
        self.__size = size
        self.__weight = weight
        self.__dimension = dimension
    
    def set_species(self,species):
        self.__species = species

    def set_name(self,name):
        self.__name = name

    def set_size(self,size):
        self.__size = size
    
    def set_weight(self,weight):
        self.__weight = weight

    def set_dimension(self,dimension):
        self.__dimension = dimension

    def get_species(self):
        return self.__species

    def get_name(self):
        return self.__name
    
    def get_size(self):
        return self.__size

    def get_weight(self):
        return self.__weight

    def get_dimension(self):
        return self.__dimension    

    def __str__(self):
        return f"""\nSpecies :{self.__species}\nName :{self.__name}\nSize in meters :{self.__size}\nWeight in kg :{self.__weight}\nDimension in m square :{self.__dimension}"""









    

