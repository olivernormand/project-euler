import numpy as np

str1 = '5H 5H 5C 8H 8H'

value_interpret = {
    0: 'high card', 
    1: 'one pair', 
    2: 'two pairs', 
    3: 'three of a kind',
    4: 'straight', 
    5: 'flush', 
    6: 'full house', 
    7: 'four of a kind', 
    8: 'straight flush', 
    9: 'royal flush',
}

suit_value = {
    'C': 0, 
    'D': 1, 
    'H': 2, 
    'S': 3,
}

class PokerHand():

    def __init__(self, cards):
        self.values, self.suits = self.return_values_suits(cards)
        self.hand, self.hand_value = self.return_hand()

    def return_hand(self):
        
        hand_exists = self.compute_full_house()
        if hand_exists:
            return 6, hand_exists

        hand_exists = self.compute_flush()
        if hand_exists:
            return 5, hand_exists

        hand_exists = self.compute_straight()
        if hand_exists:
            return 4, hand_exists

        hand_exists = self.compute_three_of_a_kind()
        if hand_exists:
            return 3, hand_exists

        hand_exists = self.compute_two_pair()
        if hand_exists:
            return 2, hand_exists

        hand_exists = self.compute_one_pair()
        if hand_exists:
            return 1, hand_exists
        
        hand_exists = self.compute_high_card()
        if hand_exists:
            return 0, hand_exists


    def return_values_suits(self, hand_as_string):
        hand = hand_as_string.split(' ')

        values = [None] * 5
        suits = [None] * 5

        for i in range(5):
            value, suit = hand[i]

            if value == 'J':
                value = 11
            elif value == 'Q':
                value = 12
            elif value == 'K':
                value = 13
            elif value == 'A':
                value = 14

            value = int(value)

            values[i] = value
            suits[i] = suit

        values = np.array(values)
        suits = np.array(suits)

        ind = np.argsort(values)

        return values[ind], suits[ind]

    def compute_high_card(self):
        return np.max(self.values)
    
    def compute_one_pair(self):
        count = 0
        value = None
        for i in range(1,5):
            if self.values[-i] == self.values[-i - 1]:
                count += 1
                value = self.values[-i]

        if count == 1:
            return value 
        else:
            return None

    def compute_two_pair(self):
        count = 0
        value = 0 

        for i in range(1,5):
            cond1 = self.values[-i] == self.values[-i - 1]
            cond2 = value != self.values[-i]
            if cond1 and cond2:
                count += 1
                if count == 2:
                    max_value = value
                value = self.values[-i]
            
        if count == 2:
            return max_value 
        else:
            return None 

    def compute_three_of_a_kind(self):
        count = 0
        value = 0

        for i in range(1, 4):
            if self.values[-i] == self.values[-i - 1]:
                value = self.values[-i]
                if self.values[-i - 2] == value:
                    count += 1
        
        if count == 1:
            return value
        else:
            return None

    def compute_straight(self):
        diff = np.diff(self.values)
        if np.all(diff == 1):
            return np.max(self.values)
        else:
            return None
    
    def compute_flush(self):
        unique_suits = np.unique(self.suits)
        if len(unique_suits) == 1:
            return suit_value[unique_suits[0]] 
        else:
            return None

    def compute_full_house(self):
        three_of_a_kind = self.compute_three_of_a_kind()
        pair = self.compute_one_pair()

        print(three_of_a_kind, pair)
        if three_of_a_kind:
            if pair:
                return [three_of_a_kind, pair]
        else:
            return None


my_hand = PokerHand(str1)
print(my_hand.values, my_hand.suits)
print(my_hand.hand, my_hand.hand_value)

