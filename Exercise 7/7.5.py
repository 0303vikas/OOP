# File:  Exercise7_5_Vikas_singh.py
# Author: Vikas Singh       
# Description:  Simplified code for relationship between students and their pets

# Student class stores the all the details for the student
class Student:
    # init function stores details of the student or current state of the class
    def __init__(self,first_name,last_name,student_ID):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__student_ID = student_ID
        self.__pets = []

    # set first name of the student
    def set_first_name(self,first_name):
        self.__first_name = first_name

    # get first name of the student
    def get_first_name(self):
        return self.__first_name

    # set last name of the student
    def set_last_name(self,last_name):
        self.__last_name = last_name

    # get last name of the student    
    def get_last_name(self):
        return self.__last_name

    # set the student id of the student
    def set_student_ID(self,student_ID):
        self.__student_ID = student_ID

    # get the student id of the student
    def get_student_ID(self):
        return self.__student_ID

    # add pets to the pet array
    # gets input and set the state of the pet class and
    # append the current state of the pet class in the array
    def add_pets(self,species,name):
        self.__pets.append(Pet(species,name))
    
    # removes pets from the array
    def remove_pets(self):
        # for removing all the pets
        #for i in range(0,len(self.__pets)+1):
        #    self.__pets.remove(i)

        # for removing just one pet
        self.__pets.remove(0)

    # print pets from the array
    def print_pets(self):
        for i in self.__pets:
            print(i)

    # returns the current state of the class    
    def __str__(self):
        return "Id of the student : " + str(self.__student_ID) + "\nName of the student : " + str(self.__first_name) +" " + str(self.__last_name)


# class Pet stores the details of the pet owned by the students
class Pet:
    # contains the current state of the class
    def __init__(self, species,name):
        self.__species = species
        self.__name = name

    # set the species of the pet
    def set_species(self,species):
        self.__species = species

    # get the species of the pet
    def get_species(self):
        return self.__species

    # set the name of the pet
    def set_name(self,name):
        self.__name = name

    # get the name of the pet
    def get_name(self):
        return self.__name

    # returns the current state of the function
    def __str__(self):
        return "\nPet species : " + str(self.__species) + "\nPet name : " + str(self.__name)


# main function
def main():
    # details of student 1 and pets owned by them
    student1 = Student("Vikas","Singh","10212")
    student1.add_pets("Cat","Tiger")
    student1.add_pets("King","kong")
    # print student details
    print(student1)
    # print details of students pets
    print('\nDetails of pets')
    student1.print_pets()

# initiate the function
main()




