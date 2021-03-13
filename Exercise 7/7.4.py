# File:         main.py
# Author: Vikas Singh       
# Description:  Deck of cards and card games.

import card
import deck

class PlayerScore:

    def __init__(self,player1,player2,player3):
        self.__player1 = player1
        self.__player2 = player2
        self.__player3 = player3

    def set_player_1(self,player1):
        self.__player1 = player1
    
    def set_player_2(self,player2):
        self.__player2 = player2
    
    def set_player_3(self,player3):
        self.__player3 = player3

    def get_player_1(self):
        return self.__player1
    
    def get_player_2(self):
        return self.__player2
    
    def get_player_3(self):
        return self.__player3



def main():
    
    print("Let's test that a single card works...")
    
    my_card = card.Card("Hearts", 12)
    my_card.show_card()
    print(my_card)

    print("Single card testing is over.\n")

    print("Let's test that a deck of card is created...")

    my_deck = deck.Deck()
    my_deck.show_deck()

    print("Card deck testing is over.\n")

    print("Let's shuffle the deck.")
    my_deck.shuffle_deck()

    print("Let's test that a deck of card is shuffled...")

    my_deck.show_deck()

    print("Cards should be suffled now.\n")

    print("Let's draw 2 cards and show them.")
    print("You draw:")
    card1 = my_deck.draw_card()
    card1.show_card()
    print("Your opponent draw:") 
    card1 = my_deck.draw_card()
    card1.show_card()
    
    # Code your Exercise 7 taks 4 game here. 

    print("\n######## Game begins for 3 players ########\n")
    print(" Drawing card for Player 1....")
    player_1_card = my_deck.draw_card()
    player_1_card.show_card()

    print("\n Drawing card for Player 2....")
    player_2_card = my_deck.draw_card()
    player_2_card.show_card()

    print("\n Drawing card for Player 3....")
    player_3_card = my_deck.draw_card()
    player_3_card.show_card()

    while True:
        if player_1_card.card_number != player_2_card.card_number != player_3_card.card_number:
            print("Result of the game....")
            if int(player_1_card.card_number) >int(player_2_card.card_number) and int(player_1_card.card_number) > int(player_3_card.card_number):
                print('Player 1 wins...')
                if int(player_2_card.card_number) > int(player_3_card.card_number):
                    print("Player 2 get's second position...")
                    print('Player 3 looses the match')
                else:
                    print("Player 3 get's second position...")
                    print('Player 2 looses the match')
            elif player_2_card.card_number > player_1_card.card_number and player_2_card.card_number > player_3_card.card_number:
                print('Player 2 wins...')
                if int(player_1_card.card_number) > int(player_3_card.card_number):
                    print("Player 1 get's second position...")
                    print('Player 3 looses the match')
                else:
                    print("Player 3 get's second position...")
                    print('Player 1 looses the match')
            else:
                print('Player 3 wins...')
                if int(player_1_card.card_number) > int(player_2_card.card_number):
                    print("Player 1 get's second position...")
                    print('Player 2 looses the match')
                else:
                    print("Player 2 get's second position...")
                    print('Player 1 looses the match')
            return False
        elif player_1_card.card_number == player_2_card.card_number or player_2_card.card_number == player_3_card.card_number or player_3_card.card_number == player_1_card.card_number:
            print('\nThere was a tie...\n')
            if player_1_card.card_number == player_2_card.card_number:
                print('\nPlayer 1 and Player 2 tied\n')
            elif player_2_card.card_number == player_3_card.card_number:
                print('\nPlayer 1 and Player 2 tied\n')
            elif player_3_card.card_number == player_1_card.card_number:
                print('\nPlayer 1 and Player 2 tied\n')
            else:
                print('\nPlayer 1, Player 2 and Player 3 tied\n')
            
            print('\n######## Re-match ########')

            print(" Drawing card for Player 1....")
            player_1_card = my_deck.draw_card()
            player_1_card.show_card()

            print("\n Drawing card for Player 2....")
            player_2_card = my_deck.draw_card()
            player_2_card.show_card()

            print("\n Drawing card for Player 3....")
            player_3_card = my_deck.draw_card()
            player_3_card.show_card()
            
            
            
            

            





    

    

# Calling the main function here, do not change...
main()
