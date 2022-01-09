from random import shuffle


class cards:
    def __init__(self,values,suits):
        self.values=values
        self.suits=suits

    def __repr__(self):
        return f"{self.values} of {self.suits}"

class deck:
    def __init__(self):
        suits=["Hearts", "Dimonds", "Spades", "Club"]
        Values=["A","2","3","4","5","6","7","8","9","10","J","K","Q"]
        self.cards=[cards(Values,suits) for suit in suits for value in Values]
        print(self.cards)

    def __repr__(self):
        return f"deck {self.count()} of cards  "

    def count(self):
        return len(self.cards)

    def _deal(self,num):
        count=self.count()
        actual=min([count,num])
        if count==0:
            raise ValueError("there are no cards left")
        cards=self.cards[-actual:]
        self.cards=self.cards[:-actual]
        return cards

    def deal_cards(self):
        return self._deal(1)[0]

    def deal_hand(self,hand_size):
        return self._deal(hand_size)

    def shuffle(self):
        if self.count() < 52:
            return ValueError("only full deck can be shuffled ")
        shuffle(self.cards)
        return self

d=deck()
d.shuffle()
card=d.deal_hands()
print(cards)
hand=d.deal_hand(50)
card2=d.deal_cards()
print(card2)
print(d.cards)
cards2=d.deal_cards()


        


    
