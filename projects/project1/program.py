import random
from datastructures.bag import Bag
from card import Card, CardSuit, CardFace

def main():
    card_suits = [suit.value for suit in list(CardSuit)]
    card_suit = []
    for suit in list(CardSuit):
        card_suit.append(Card(suit.value))

    print(card_suit)



class Game:
    def __init__(self,player, dealer):
        self.__playerScore__=0
        self.__dealerScore__=0
        self.__player__=player
        self.__dealer__=dealer
        main()
    
    def shuffleCards(self):
        numOfDecks= 1