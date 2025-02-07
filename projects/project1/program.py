import random
from datastructures.bag import Bag
from project1.card import Card, CardSuit, CardFace

def main():
    card_suits = [suit.value for suit in list(CardSuit)]
    cards = []
    for suit in list(CardSuit):
        for face in list(CardFace):
            cards.append(Card(suit.value, face.value))

    print(cards)



class Game:
    def __init__(self,player, dealer):
        self.__playerScore__=0
        self.__dealerScore__=0
        self.__player__=player
        self.__dealer__=dealer
        main()
    
    def shuffleCards(self):
        numOfDecks= 1