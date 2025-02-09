import copy
import random
from datastructures.bag import Bag
from projects.project1.card import Card, CardSuit, CardFace

def main():
    one_deck_list = [Card(face, suit) for suit in CardSuit for face in CardFace]
    print(f"One deck has {len(one_deck_list)} cards")
    print("".join(str(card) for card in one_deck_list))

    deck_count = random.choice([2, 4, 6, 8])
    multi_deck_list = [card for _ in range(deck_count) for card in copy.deepcopy(one_deck_list)]

    print(f"{deck_count} decks have {len(multi_deck_list)} cards")
    print("".join(str(card) for card in multi_deck_list))

    deck_bag = Bag(*multi_deck_list)
    print(list(deck_bag.distinct_items()))
    two_cards = random.sample(list(deck_bag.distinct_items()), 2)
    print(f"Two cards: {"".join(str(card) for card in two_cards)} with a face value of: {sum(card.face.face_value() for card in two_cards)}")

if __name__ == '__main__':
    main()

"""import random
from datastructures.bag import Bag
from projects.project1.card import Card, CardSuit, CardFace

class Game:
    def __init__(self,player, dealer):
        self.__playerScore__=0
        self.__dealerScore__=0
        self.__player__=player
        self.__dealer__=dealer


    def main():
        number=random.randint(2,8)
        card_suits = [suit.value for suit in list(CardSuit)]
        print(card_suits)
        cards = []
        for i in range(2):
            for face in list(CardSuit):
                for suit in list(CardFace):
                    cards.append(suit)
        print(cards)
        print(len(cards))
    main()

if __name__ == '__main__':
    Game"""

