from enum import Enum
from datastructures.bag import Bag


bag = Bag()

class CardSuit(Enum):
    HEARTS = ""
    SPADE = ""
    CLUBS = ""
    DIAMONDS = ""

class CardFace(Enum):
    ONE = "1"
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    SEVEN = "7"
    EIGHT= "8"
    NINE = "9"
    JACK="10"
    QUEEN="10"
    KING = "10"
    ACE="1" #keep in mind an ace can also be an eleven if paired with a face card
    


class Card:
    card_face: CardFace
    card_suit: CardSuit