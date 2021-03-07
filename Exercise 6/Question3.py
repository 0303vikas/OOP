# -*- coding: utf-8 -*-

"""

@File name: Exercise_6_3_Vikas_singh.py
@Author: Vikas singh
@description: Inherit class mammal

"""
#import class mammal
from Exercise_4_8_Vikas_singh import Mammal 

# Sound_diet class that inherits mammal class
class Sound_diet(Mammal):
    # init the sound_diet class
    def __init__ (self,Species,name,size,weight,dimension,diet,sound):        
        # add super to inherit all the properties from the parent class mammal
        super().__init__(Species,name,size,weight,dimension)
        # add sound and diet to the animal object 
        self.__animal_sound = sound
        self.__animal_diet = diet



    # print the output
    def __str__(self):
        return super().__str__() + "\nSound made by the animal is :" + str(self.__animal_sound) + "\nDiet of the animal in calories :" + str(self.__animal_diet)

# main function
def main():
    
    # making 3 animal object from class mammal1,mammal2, mammal3
    mammal1 = Sound_diet('Bear','Brown Bear','3','250','4.5',"10000calories","growl")
    
    mammal2 = Sound_diet('Wolf','Arctic wolf','1.5','50','1.2',"7000calories","owooooo")
    
    mammal3 = Sound_diet('Cat','Indian Tiger','3','220','3',"8000calories","meow")

    ### if your have to input all the details of the animal ####
    # print('Give the details for the first animal')
    # mammal1_species = input('The name of the species')
    # mammal1_name = input('The name of the animal')
    # mammal1_size = input('The size of the mammal')
    # mammal1_weight = input('The weight of the mammal')
    # mammal1_dimension = input('The dimension of the mammal')
    # mammal1_diet = input('The diet of the animal')
    # mammal1_sound = input('The sound of the animal')
    # mammal1 = Sound_diet(mammal1_species,mammal1_name,mammal1_size,mammal1_weight,mammal1_dimension,mammal1_diet,mammal1_sound)

    # printing the result
    print('\nDetails of the animals are 1 are...\n ')
    print(mammal1)
    print('\nDetails of the animals are 2 are...\n ')
    print(mammal2)
    print('\nDetails of the animals are 3 are...\n ')
    print(mammal3)

main()