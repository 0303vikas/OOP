import random
import card

class Deck:

    def __init__(self):
        self.__cards = []
        self.create_card()


    def create_card(self):
        for suit in ["Diamonds","Hearts","Clubs","Spades"]:
            for numb in range(1,14):
                self.__cards.append(card.Card(suit,numb))

    def show_deck(self):
        for i in self.__cards:
            i.show_card()
    
    def shuffle_deck(self):
        random.shuffle(self.__cards)

    def draw_card(self):
        return random.choice(self.__cards)

    

    




            
        

