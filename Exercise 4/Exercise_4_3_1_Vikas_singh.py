from Exercise_4_3_Vikas_singh import *
from Exercise_3_5_Vikas_singh import *

# main function
def main():   
    #user input for cell phone details
    cell_phone_manufacturer = input('Enter the manufacturer: ')
    cell_phone_model = input('Enter the model number: ')
    cell_phone_price = input('Enter the retail price: ')

    # init the class and create an object
    cell_phone = CellPhone(cell_phone_manufacturer,cell_phone_model,cell_phone_price)   
   
    
    print("Now for the second cell phone.")
    #user input for cell phone details of the second device
    cell_phone_manufacturer1 = input('Enter the manufacturer: ')
    cell_phone_model1 = input('Enter the model number: ')
    cell_phone_price1 = input('Enter the retail price: ')

    # init the class and create another object
    cell_phone1 = CellPhone(cell_phone_manufacturer1,cell_phone_model1,cell_phone_price1)   
    

    print("Now for the third cell phone.")
    #user input for cell phone details of the second device
    cell_phone_manufacturer2 = input('Enter the manufacturer: ')
    cell_phone_model2 = input('Enter the model number: ')
    cell_phone_price2 = input('Enter the retail price: ')

    # init the class and create another object
    cell_phone2 = CellPhone(cell_phone_manufacturer2,cell_phone_model2,cell_phone_price2)
   

    print("Now for the fourth cell phone.")
    #user input for cell phone details of the second device
    cell_phone_manufacturer3 = input('Enter the manufacturer: ')
    cell_phone_model3 = input('Enter the model number: ')
    cell_phone_price3 = input('Enter the retail price: ')

    # init the class and create another object
    cell_phone3 = CellPhone(cell_phone_manufacturer3,cell_phone_model3,cell_phone_price3)
   
    print("Now for the fifth cell phone.")
    #user input for cell phone details of the second device
    cell_phone_manufacturer4 = input('Enter the manufacturer: ')
    cell_phone_model4 = input('Enter the model number: ')
    cell_phone_price4 = input('Enter the retail price: ')

    # init the class and create another object
    cell_phone4 = CellPhone(cell_phone_manufacturer4,cell_phone_model4,cell_phone_price4)
   
    print("Now for the sixth cell phone.")
    #user input for cell phone details of the second device
    cell_phone_manufacturer5 = input('Enter the manufacturer: ')
    cell_phone_model5 = input('Enter the model number: ')
    cell_phone_price5 = input('Enter the retail price: ')

    # init the class and create another object
    cell_phone5 = CellPhone(cell_phone_manufacturer5,cell_phone_model5,cell_phone_price5)
    
    print('Now rolling the dice.')
    # initialize the class dice
    roll_dice = Dice()

    roll_dice.roll_dice()
    print(roll_dice)

    # if the side one is up on dice, then cell phone 1 is printed,
    # else if side 2 is up , cell phone 2 is printed
    # else if side 3 is up , cell phone 3 is printed
    # else if side 4 is up, cell phone 4 is printed
    # else if side 5 is up, cell phone 5 is printed
    # else if side 6 is up, cell phone 6 is printed
    if int(roll_dice.side) == 1:
        print('The selected cell phone is, Cell-Phone number 1 :')
        print(cell_phone)
    elif int(roll_dice.side) == 2:
        print('The selected cell phone is, Cell-Phone number 2 :')
        print(cell_phone1)
    elif int(roll_dice.side) == 3:
        print('The selected cell phone is, Cell-Phone number 3 :')
        print(cell_phone2)
    elif int(roll_dice.side) == 4:
        print('The selected cell phone is, Cell-Phone number 4 :')
        print(cell_phone3)
    elif int(roll_dice.side) == 5:
        print('The selected cell phone is, Cell-Phone number 5 :')
        print(cell_phone4)
    else:
        print('The selected cell phone is, Cell-Phone number 6 :')
        print(cell_phone5)



    
main()