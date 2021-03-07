# -*- coding: utf-8 -*-

""" 
@File name: Exercise_3_5_Vikas_singh.py
@Author: Vikas Singh
@description: giving mammels to student

"""

import random
import Exercise_4_8_Vikas_singh as mam # inport mammal class 

# main class student
class Student(object):
    id_count = 1 # keeps the count of student id 

    def __init__(self,fname,lname):
        self.__studentid = Student.id_count
        self.__firstname = fname
        self.__lastname = lname        
        
        Student.id_count += 1 # increment id for each new object created from class student

    #set the first name of the student
    def set_fname(self,fname):
        self.__firstname = fname
    
    #set the last name of the student
    def set_lname(self,lname):
        self.__lastname = lname   
    
    #get the id of the student
    def get_id(self):
        return self.__studentid
    #get he first name of the student
    def get_fname(self):
        return self.__firstname
    #get the last name of the student
    def get_lname(self):
        return self.__lastname    

    def __str__(self):
        return f"""Student_id: {self.__studentid}\nStudent_first_name: {self.__firstname}\nStudent_last_name: {self.__lastname}\n"""

# function to make 4 different student
def make_student():
    # dictionary where all the information will be stored
    my_student_dict = {}

    # ask for 4 student name's and their mammals name from user
    # loop will run four times
    for i in range(1,5):
        print('For Student', i)

        first_name = input('First Name :')
        second_name = input('Second Name :')
        student_pet_species = input("Student's pet species :")
        student_pet_name = input("Student's pet name :")
        student_pet_size = input("Student's pet size :")
        student_pet_weight = input("Student's pet weight :")
        student_pet_dimension = input("Student's pet dimensions :")

        #init the class student and mammal create 4 player objects and 4 mammal object
        student_class = Student(first_name,second_name)
        mammal_class = mam.Mammal(student_pet_species,student_pet_name,student_pet_size,student_pet_weight ,student_pet_dimension)
        

        # users student id as key and 'student object and mammal object 'as values and put them in dictionary
        my_student_dict[student_class.get_id()] = [student_class,mammal_class]
        

    
    # init show result function 
    # that shows the details of different students
    show_result(my_student_dict)
    


# shown details of each student
def show_result(student_dict):

    for i in student_dict.values():
        print("\nStudent details")        
        print(i[0])
        print("\nStudent's pet details.")
        print(i[1])
        print()
        
# main function
def main():
    # init make student function
    make_student()   
    

main()


    

