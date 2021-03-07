# -*- coding: utf-8 -*-

"""

@File name: Exercise_4_3_Vikas_singh.py
@Author: Vikas singh
@description: Seperating python code in two files

"""



class CellPhone(object):
    # to keep a count of the id 
    id_count = 1    

    def __init__(self,manu,mod,ret):
        self.manufacturer = manu
        self.model = mod
        self.retail = ret
        self.id = CellPhone.id_count
        CellPhone.id_count += 1    
        

    #set the manufacturing name
    def set_Manufact(self,manufact_name):
        self.manufacturer = manufact_name
    # set the modal name
    def set_Model(self,model_name):
        self.model = model_name
    # set the retail price
    def set_RetailPrice(self,price):
        self.retail = price

    def set_Id(self, id):
        self.id = id
    # get manufacturing details
    def get_Manufact(self):
        return self.manufacturer
    # get model name
    def get_Model(self):
        return self.model
    # get retail price
    def get_RetailPrice(self):
        return self.retail
    # get the id of the object
    def get_Id(self):
        return self.id 
    # print out the current value of the data attributes of the class
    def __str__(self):
        return f"""Manufacturer: {self.manufacturer}\nModel number: {self.model}\nRetail: {self.retail}\nId: {self.id}"""



