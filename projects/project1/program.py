import copy
import random
from datastructures.bag import Bag
from projects.project1.card import Card, CardSuit, CardFace

class Game:

    def main():
        one_deck_list = [Card(face, suit) for suit in CardSuit for face in CardFace]
        print(f"One deck has {len(one_deck_list)} cards")
        print("".join(str(card) for card in one_deck_list))

        deck_count = random.choice([2, 4, 6, 8])
        multi_deck_list = [card for _ in range(deck_count) for card in copy.deepcopy(one_deck_list)]

        print(f"{deck_count} decks have {len(multi_deck_list)} cards")
        print("".join(str(card) for card in multi_deck_list))

        deck_bag = Bag(*multi_deck_list)
        print(deck_bag.distinct_items())
        print(deck_bag)
        two_cards = random.sample(list(deck_bag.distinct_items()), 2)
        print(f"Two cards: {"".join(str(card) for card in two_cards)} with a face value of: {sum(card.card_face.face_value() for card in two_cards)}")

    if __name__ == '__main__':
        main()

