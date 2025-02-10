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
    print("\n")
    deck_bag=[] #This will clear everything
    playerCards=[]
    dealerCards=[]

    one_deck_list = [Card(face, suit) for suit in CardSuit for face in CardFace]

    deck_count = random.choice([2, 4, 6, 8])
    multi_deck_list = [card for _ in range(deck_count) for card in copy.deepcopy(one_deck_list)]

    deck_bag = Bag(*multi_deck_list)

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
    #P is player and D is Dealer
    #Following initializes the game mechanics
    turn="P" 
    playerStatus= "Playing"
    dealerStatus= "Playing"

    while (playerScore < 22 and dealerScore < 22) and (playerStatus == "Playing" or dealerStatus == "Playing"):
        #The following happens during players turn
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
        #The following happens during the dealers turn
        if turn == "D" and dealerStatus == "Playing":
            if dealerScore < 17:
                newCard=random.choice(list(deck_bag.distinct_items()))
                dealerCards.append(newCard)
                deck_bag.remove(newCard)
                dealerScore= sum(card.card_face.face_value() for card in dealerCards)
                print("Dealer's Hand:", dealerCards[0], (len(dealerCards)-1)*"[Hidden]"," | Score:",dealerCards[0].card_face.face_value())
            
            if playerStatus == "Playing":
                turn = "P"
            else:
                dealerStatus = "Stay"
                turn= "P"
        else:
            turn="P"
    print("------------------------------------------------------------------------") #line break

    #The following happens when either both players stay or one goes over 21 points (and all the different circumstances).
    if playerStatus == "Stay" and dealerStatus == "Stay":
        if playerScore > dealerScore:
            print("Player wins! Congrats!")
            endGame(playerCards,playerScore,dealerCards,dealerScore)
        if playerScore == dealerScore:
            print("It's a tie!")
            endGame(playerCards,playerScore,dealerCards,dealerScore)
    if playerStatus == "Won":
            print("Player wins! Congrats!")
            endGame(playerCards,playerScore,dealerCards,dealerScore)
    if dealerStatus == 21:
            print("Dealer got a BlackJack. Player Lost!")
            endGame(playerCards,playerScore,dealerCards,dealerScore)
    if playerScore>21 and dealerScore < 22:
        print("Player Bust! Dealer Wins!")
        endGame(playerCards,playerScore,dealerCards,dealerScore)
    if dealerScore>21 and playerScore < 22:
        print("Dealer Bust! Player Wins, Congrats!")
        endGame(playerCards,playerScore,dealerCards,dealerScore)
    else:
        print("It's a tie! Both Player's Bust!")
        endGame(playerCards,playerScore,dealerCards,dealerScore)

 

#The prompt to end the game (or continue)!        
def endGame(playerCards,playerScore,dealerCards,dealerScore):
    print("🃏 Final Hands")
    print(f"Player's Hand: {"".join(str(card) for card in playerCards)} | Score: {playerScore}")
    print(f"Dealer's Hand: {"".join(str(card) for card in dealerCards)} | Score: {dealerScore}")

    userInput=input("Would you like to play again?(Y)es or (N)o?").upper()
    if userInput == "Y":
        main()
    if userInput == "N":
            exit()
    else:
        print("Please input either Y for Yes or N for No.")




                
        


if __name__ == '__main__':
    print("🎮 Welcome to BlackJack!")
    main()

