#my new project on py
import random

class Deck:
    def __init__(self):
        #for acessing cards variable in all the functions use self
        self.cards = []
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        #ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        ranks = [
            {"rank" : "A", "value" : 11},
            {"rank" : "2", "value" : 1},
            {"rank" : "3", "value" : 2},
            {"rank" : "4", "value" : 3},
            {"rank" : "5", "value" : 4},
            {"rank" : "6", "value" : 5},
            {"rank" : "7", "value" : 6},
            {"rank" : "8", "value" : 7},
            {"rank" : "9", "value" : 8},
            {"rank" : "10", "value" : 9},
            {"rank" : "J", "value" : 10},
            {"rank" : "Q", "value" : 10},
            {"rank" : "K", "value" : 10},
        ]
        #for appending the suits and ranks in self.cards for creating the deck
        for suit in suits:
            for rank in ranks:
                self.cards.append([suit, rank])

    #function for shuffling the cards for creating the perfect deck of 52 cards
    def shuffle(self):
        random.shuffle(self.cards)

    #function for returning one card out of the deck of cards
    def deal(self, number):
        cards_dealt = []
        for x in range(number):
            card = self.cards.pop()
            cards_dealt.append(card)
        return cards_dealt


deck1 = Deck()
deck2 = Deck()
deck2.shuffle
print(deck1.cards)
print(deck2.cards)




# for testing purpose:
# shuffle()
# cards_dealt = deal(2)
# card = cards_dealt[0]
# rank = card[1]
# print(card)

# if rank == "A":
#     value = 11
# elif rank == "J":
#     value = 10


