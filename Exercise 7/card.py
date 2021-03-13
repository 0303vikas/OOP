class Card:

    def __init__(self,name,number):
        self.__card_suit = name
        self.card_number = number

    
    def show_card(self):
        print(self.card_number,' of ',self.__card_suit)

    def __str__(self):
        return "Card is " + str(self.card_number) + " of " + str(self.__card_suit)





