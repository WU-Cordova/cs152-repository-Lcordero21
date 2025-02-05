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


class Card:
    card_face: CardFace
    card_suit: CardSuit