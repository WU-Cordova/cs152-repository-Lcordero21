import copy
import random
from datastructures.bag import Bag
from projects.project1.card import Card, CardSuit, CardFace


playerCards=[]
playerScore=0
dealerCards=[]
dealerScore=0
deck_bag=[]

def main():
    #The below code initializes the decks we are pulling from 
    deck_bag=[] #This will clear 

    one_deck_list = [Card(face, suit) for suit in CardSuit for face in CardFace]
    print(f"One deck has {len(one_deck_list)} cards")

    deck_count = random.choice([2, 4, 6, 8])
    multi_deck_list = [card for _ in range(deck_count) for card in copy.deepcopy(one_deck_list)]
    print(f"{deck_count} decks have {len(multi_deck_list)} cards")

    deck_bag = Bag(*multi_deck_list)

    #Can delete the below code after done with project!!
    two_cards = random.sample(list(deck_bag.distinct_items()), 2)
    print(two_cards)
    print(f"Two cards: {"".join(str(card) for card in two_cards)} with a face value of: {sum(card.card_face.face_value() for card in two_cards)}")

    #Below I start actual BagJack stuff
    print("🃏 Initial  Deal:")

    #Initilaizes Player
    playerCards=random.sample(list(deck_bag.distinct_items()), 2)
    playerScore= sum(card.card_face.face_value()for card in playerCards)

    for item in playerCards:
        deck_bag.remove(item)


    if playerScore > 21:
        playerScore -= 10

    print(f"Player's Hand: {"".join(str(card) for card in playerCards)} | Score: {playerScore}")

        


    #Initializes Dealer
    dealerCards=random.sample(list(deck_bag.distinct_items()), 2)
    dealerScore=sum(card.card_face.face_value()for card in dealerCards)

    for item in dealerCards:
        deck_bag.remove(item)

    if dealerScore > 21:
        dealerScore -= 10

    print(f"Dealer's Hand: {dealerCards[0]} [Hidden] | Score: {dealerCards[0].card_face.face_value()}")

    game(playerScore,dealerScore,deck_bag,playerCards,dealerCards)

def game(playerScore,dealerScore,deck_bag,playerCards,dealerCards):
    turn="P" #P is player and D is Dealer
    playerStatus= "Playing"
    dealerStatus= "Playing"
    while (playerScore < 22 and dealerScore < 22) and (playerStatus == "Playing" or dealerStatus == "Playing"):
        if turn == "P" and playerStatus == "Playing":
            if playerScore != 21:
                userinput=input("Would you like to (H)it or (S)tay?").upper()
                if userinput == "H":

                    newCard=random.choice(list(deck_bag.distinct_items()))
                    playerCards.append(newCard)
                    deck_bag.remove(newCard)

                    playerScore= sum(card.card_face.face_value() for card in playerCards)
                    print(f"Player's Hand: {"".join(str(card) for card in playerCards)} | Score: {playerScore}")

                    if dealerStatus == "Playing":
                        turn="D"

                elif userinput == "S":
                    playerStatus = "Stay"
                    turn = "D"
                else:
                    print("Please input either H for Hit or S for Stay.")
            else:
                playerStatus="Won"
                dealerStatus="Lost"
        else:
            turn = "D"
        if turn == "D" and dealerStatus == "Playing":
            if dealerScore != 21:
                if dealerScore < 17:
                    newCard=random.choice(list(deck_bag.distinct_items()))
                    dealerCards.append(newCard)
                    deck_bag.remove(newCard)

                    


                
        


if __name__ == '__main__':
    main()

