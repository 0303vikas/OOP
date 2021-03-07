# -*- coding: utf-8 -*-

"""

@File name: Exercise_6_3_Vikas_singh.py
@Author: Vikas singh
@description: Inherit class mammal

"""

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

class Domestic(Mammal):

    def __init__(self,Species,name,size,weight,dimension,diet,sound):
        super().__init__(Species,name,size,weight,dimension)
        self.__animal_sound = sound
        self.__animal_diet = diet

    def __str__(self):    
        return super().__str__() + "\nSound made by the animal is :" + str(self.__animal_sound) + "\nDiet of the animal in calories :" + str(self.__animal_diet)


class Wild(Mammal):

    def __init__(self,Species,name,size,weight,dimension,diet,sound):
        super().__init__(Species,name,size,weight,dimension)
        self.__animal_sound = sound
        self.__animal_diet = diet

    def __str__(self):    
        return super().__str__() + "\nSound made by the animal is :" + str(self.__animal_sound) + "\nDiet of the animal in calories :" + str(self.__animal_diet)




# main function
def main():
    
    # making 3 animal object from class mammal1,mammal2, mammal3
    mammal1 = Wild('Bear','Brown Bear','3','250','4.5',"10000calories","growl")
    
    mammal2 = Domestic('Cat','Indian Tiger','3','220','3',"8000calories","meow")  


    # printing the result
    print('\nDetails of the Wild animal are...\n ')
    print(mammal1)
    print('\nDetails of the Domestic animal are...\n ')
    print(mammal2)
    
main()