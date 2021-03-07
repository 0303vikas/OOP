# -*- coding: utf-8 -*-

"""

@File name: Exercise_6_3_Vikas_singh.py
@Author: Vikas singh
@description: Inherit class for student and teacher from OOP class

"""
# main class OOP parent class
class OOP:
    # function to save the state of the class
    def __init__(self,coursename,startdate,enddate):
        self.__coursename = coursename
        self.__coursestartdate = startdate
        self.__courseenddate = enddate
    # function to return the current state of the class
    def __str__(self):
        return f"""\nCourse Name : {self.__coursename}\nCourse Start Date: {self.__coursestartdate}\nCourse End Date: {self.__courseenddate}"""

# child function that inherits from the main class
class Student(OOP):
    # constructor
    def __init__(self,coursename,startdate,enddate,studentId,studentName,exCompleted,score,passfail):
        super().__init__(coursename,startdate,enddate)
        self.__studentId = studentId
        self.__studentName = studentName
        self.__exCompleted = exCompleted
        self.__score = score
        self.__passfail = passfail
    # function to return the current state of the class
    def __str__(self):
        return super().__str__() + "\nStudent_ID :" + str(self.__studentId) + "\nStudent Name :" + str(self.__studentName) + "\nExercises Completed out of 10:" + str(self.__exCompleted) + "\nScore out of 100 :" + str(self.__score) + "\nResult of the course :" + str(self.__passfail)
        

class Teacher(OOP):
    # constructor
    def __init__(self,coursename,startdate,enddate,teacherId,teacherName,assismain):
        super().__init__(coursename,startdate,enddate)
        self.__teacher = teacherId
        self.__teacherName = teacherName
        self.__assismain = assismain
        
    # function to return the current state of the class
    def __str__(self):
        return super().__str__() + "\nTeacher_ID :" + str(self.__teacher) + "\nTeacher Name :" + str(self.__teacherName) + "\nTeacher Position :" + str(self.__assismain) 



# child class for domestic animal inherit of class Mammal
class Domestic_student_animal(Student):
    #Initation of the class 
    def __init__(self,Species,name,size,weight,dimension,diet,sound):        
        self.__species = Species
        self.__name = name
        self.__size = size
        self.__weight = weight
        self.__dimension = dimension
        self.__animal_sound = sound
        self.__animal_diet = diet
    # return the sound and diet of the animal
    def __str__(self):    
        return f"""\nSpecies :{self.__species}\nName :{self.__name}\nSize in meters :{self.__size}\nWeight in kg :{self.__weight}\nDimension in m square :{self.__dimension}\nAnimal sound :{self.__animal_sound}\nAnimal Diet :{self.__animal_diet}"""

# child class for Wild animal inherit of class Mammal
class Wild_student_animal():
    # initation of the class 
    def __init__(self,Species,name,size,weight,dimension,diet,sound):        
        self.__species = Species
        self.__name = name
        self.__size = size
        self.__weight = weight
        self.__dimension = dimension
        self.__animal_sound = sound
        self.__animal_diet = diet
    # print the sound and diet of wild animal
    def __str__(self):    
        return f"""\nSpecies :{self.__species}\nName :{self.__name}\nSize in meters :{self.__size}\nWeight in kg :{self.__weight}\nDimension in m square :{self.__dimension}\nAnimal sound :{self.__animal_sound}\nAnimal Diet :{self.__animal_diet}"""


# child class for domestic animal inherit of class Mammal
class Domestic_teacher_animal():
    #Initation of the class 
    def __init__(self,Species,name,size,weight,dimension,diet,sound):        
        self.__species = Species
        self.__name = name
        self.__size = size
        self.__weight = weight
        self.__dimension = dimension
        self.__animal_sound = sound
        self.__animal_diet = diet
    # return the sound and diet of the animal
    def __str__(self):    
        return f"""\nSpecies :{self.__species}\nName :{self.__name}\nSize in meters :{self.__size}\nWeight in kg :{self.__weight}\nDimension in m square :{self.__dimension}\nAnimal sound :{self.__animal_sound}\nAnimal Diet :{self.__animal_diet}"""

# child class for Wild animal inherit of class Mammal
class Wild_teacher_animal():
    # initation of the class 
    def __init__(self,Species,name,size,weight,dimension,diet,sound):
        self.__species = Species
        self.__name = name
        self.__size = size
        self.__weight = weight
        self.__dimension = dimension        
        self.__animal_sound = sound
        self.__animal_diet = diet
    # print the sound and diet of wild animal
    def __str__(self):    
        return f"""\nSpecies :{self.__species}\nName :{self.__name}\nSize in meters :{self.__size}\nWeight in kg :{self.__weight}\nDimension in m square :{self.__dimension}\nAnimal sound :{self.__animal_sound}\nAnimal Diet :{self.__animal_diet}"""

def main():
    # create student object
    student = Student("Object-oriented Programming","11 january 2021","30 April 2021","512653","Vikas","8","87","Pass")
    student_domestic_animal = Domestic_student_animal('Bear','Brown Bear','3','250','4.5',"10000calories","growl")
    student_wild_animal = Wild_student_animal('Cat','Indian Tiger','3','220','3',"8000calories","meow")
    # Create teacher object
    teacher = Teacher("Object-oriented Programming","11 january 2021","30 April 2021","324","Saana","Main Teacher")
    teacher_wild_animal = Wild_teacher_animal('Bear','Brown Bear','3','250','4.5',"10000calories","growl")
    teacher_domestic_animal = Domestic_teacher_animal('Cat','Indian Tiger','3','220','3',"8000calories","meow")

    # printing details of the student and teacher
    print('\nStudent details......')
    print(student)
    print('\n\nStudent domestic animal detail....\n')
    print( student_domestic_animal)
    print('\n\nStudent wild animal detail....\n')
    print(student_wild_animal)
    print('\nTeacher details......')
    print(teacher)
    print('\n\nTeacher domestic animal detail....\n')
    print( teacher_domestic_animal)
    print('\n\nTeacher wild animal detail....\n')
    print(teacher_wild_animal)
    

main()