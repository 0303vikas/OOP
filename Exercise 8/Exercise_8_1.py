# -*- coding: utf-8 -*-

""" 
@File name: Exercise_8_1_Vikas_singh.py
@Author: Vikas Singh
@description: cleaning Home

"""

# Class home that handle all the states of the room
class Home:
    # initiation method that holds the state of the things to be cleaned
    # it arguments values are either 0 or 1 
    # the arguments are further handed to set_state_home method, which
    # shows whether the things is done or not
    def __init__(self,windows,floors,bed,surfaces,fridge,toilet_paper):        
        self.__windows_state = ""
        self.__floors_state = ""
        self.__bed_state = ""
        self.__surfaces_state = ""
        self.__fridge_state = ""
        self.__toilet_paper_state = ""
        self.set_state_home(windows,floors,bed,surfaces,fridge,toilet_paper)

    # set_state_home method takes argument form the init function 
    # based on whether the arguments are zero or 1 it tells whether the 
    # room is cleaned or not
    # if the argument is 0, the its sets the element in init method to NOt cleaned
    # else if the argument is 1 it sets the element in init method to cleaned    
    def set_state_home(self,windows,floors,bed,surfaces,fridge,toilet_paper):        
        if int(windows) == 0:
            self.__windows_state = "are dirty. X"            
        else:
            self.__windows_state = "are washed. ✓"
        if int(floors) == 0:
            self.__floors_state = "are dirty. X"                      
        else:
            self.__floors_state = "are vacuumed. ✓"
        if int(bed) == 0:
            self.__bed_state = "is unmade. X"
        else:
            self.__bed_state = "is made. ✓"
        if int(surfaces) == 0:
            self.__surfaces_state = "is dusty. X"
        else:
            self.__surfaces_state = "are dusted. ✓"
        if int(fridge) == 0:
            self.__fridge_state = "is empty. X"
        else:
            self.__fridge_state = "shopping is done so fridge is full. ✓"
        if int(toilet_paper) == 0:
            self.__toilet_paper_state = "Toilet paper running out. X"
        else:
            self.__toilet_paper_state = "There is enough toilet paper. ✓"

    # method check wheather the window is cleaned or not,
    # if the window is already cleaned it will show the user the the window is alreadly cleaned
    # elif the window is set to be cleaned if the argument is 1
    # else the window is set to be dirty if the argument is 0
    def set_window_state(self,windows):
        if int(windows) == 1 and self.__windows_state == "are washed. ✓":
            print('Windows already cleaned.')
        elif int(windows) == 1:
            self.__windows_state = "are washed. ✓"
        else:
            self.__windows_state = "are dirty. X"

    # see the set_window_state comment, functionallity is similar, the only difference 
    # is that it is for the floor
    def set_floors_state(self,floors):
        if int(floors) == 1 and self.__floors_state == "are vacuumed. ✓":
            print('Floors already vaccumed.')
        elif int(floors) == 1:
            self.__floors_state = "are vacuumed. ✓"
        else:
            self.__floors_state = "dirty. X"

    # see the set_window_state comment, functionallity is similar, the only difference 
    # is that it is for the bed
    def set_bed_state(self,bed):
        if int(bed) == 1 and self.__bed_state == "is made. ✓":
            print('Bed already made.')
        elif int(bed) == 1:
            self.__bed_state = "is made. ✓"
        else:
            self.__bed_state = "is unmaid. X"

    # see the set_window_state comment, functionallity is similar, the only difference 
    # is that it is for the surface
    def set_surfaces_state(self,surfaces):
        if int(surfaces) == 1 and self.__surfaces_state == "Cleaned. ✓":
            print('Surfaces already cleaned.')
        elif int(surfaces) == 1:
            self.__surfaces_state = "Cleaned. ✓"
        else:
            self.__surfaces_state = "Not Cleaned. X"

    # see the set_window_state comment, functionallity is similar, the only difference 
    # is that it is for the fridge        
    def set_fridge_state(self,fridge):
        if int(fridge) == 1 and self.__fridge_state == "shopping is done so fridge is full. ✓":
            print('Fridge already refilled.')
        elif int(fridge) == 1:
            self.__fridge_state = "shopping is done so fridge is full. ✓"            
        else:
            self.__fridge_state = "is empty. X"

    # see the set_window_state comment, functionallity is similar, the only difference 
    # is that it is for toilet papers
    def set_toilet_state(self,toilet_paper):
        if int(toilet_paper) == 1 and self.__toilet_paper_state == "There is enough toilet paper. ✓":
            print('Toilet paper already refilled.')
        elif int(toilet_paper) == 1:
            self.__toilet_paper_state = "There is enough toilet paper. ✓"
        else:
            self.__toilet_paper_state = "Toilet paper running out. X"

    # get the current state of the window
    def get_window_state(self):
        return self.__windows_state

    # get the current state of the floor
    def get_floors_state(self):
        return self.__floors_state

    # get the current state of the bed
    def get_bed_state(self):
        return self.__bed_state

    # get the current state of the surfaces
    def get_surfaces_state(self):
        return self.__surfaces_state

    # get the current state of the fridge
    def get_fridge_state(self):
        return self.__fridge_state

    # get the current state of the toilet
    def get_toilet_state(self):
        return self.__toilet_paper_state

    # print the current state of the class home
    def __str__(self):        
        return '\nThe current state of the house is......\n' + "Windows " + self.__windows_state + "\nFloors " + str(self.__floors_state) + "\nBed "+str(self.__bed_state) + "\nSurfaces "+str(self.__surfaces_state) + "\nFridge " + str(self.__fridge_state) + "\n" + str(self.__toilet_paper_state)

# main function
def main():

    # note for the users
    print("*NOTE: ✓ means task completed, X means task incomplete.")

    # instance of class home
    house_state_1 = Home(0,0,0,0,0,0)
    # printing the instance of class home
    print(house_state_1)

    # cleaning the windows and bed/ set the window and bed to be cleaned or not cleaned
    print('\nFirst cleaning part.....')
    house_state_1.set_window_state(1)
    house_state_1.set_bed_state(1)
    print(house_state_1)

    print('\nSecond cleaning part....')
    # cleaning the floors and surfaces/ set the floor and surfaces to be cleaned or not cleaned
    house_state_1.set_floors_state(1)
    house_state_1.set_surfaces_state(1)
    print(house_state_1)
    
    print("\nThird cleaning part...")
    # for groceries
    house_state_1.set_fridge_state(1)
    print(house_state_1)

    print('\nFourth cleaning part...')
    # for toilet papers
    house_state_1.set_toilet_state(1)
    print(house_state_1)

# calling main function
main()
    

            
        


    
