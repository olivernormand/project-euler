"""
    In the game, Monopoly, the standard board is set up in the following way:

    GO	A1	CC1	A2	T1	R1	B1	CH1	B2	B3	JAIL
    H2	 	                                C1
    T2	 	                                U1
    H1	 	                                C2
    CH3	 	                                C3
    R4	 	                                R2
    G3	 	                                D1
    CC3	 	                                CC2
    G2	 	                                D2
    G1	 	                                D3
    G2J	F3	U2	F2	F1	R3	E3	E2	CH2	E1	FP


    A player starts on the GO square and adds the scores on two 6-sided dice to determine
    the number of squares they advance in a clockwise direction. Without any further rules
    we would expect to visit each square with equal probability: 2.5%. However, landing
    on G2J (Go To Jail), CC (community chest), and CH (chance) changes this distribution.

    In addition to G2J, and one card from each of CC and CH, that orders the player to go
    directly to jail, if a player rolls three consecutive doubles, they do not advance the
    result of their 3rd roll. Instead they proceed directly to jail.

    At the beginning of the game, the CC and CH cards are shuffled. When a player lands on
    CC or CH they take a card from the top of the respective pile and, after following the
    instructions, it is returned to the bottom of the pile. There are sixteen cards in each
    pile, but for the purpose of this problem we are only concerned with cards that order a
    movement; any instruction not concerned with movement will be ignored and the player will
    remain on the CC/CH square.

    Community Chest (2/16 cards):
    Advance to GO
    Go to JAIL
    Chance (10/16 cards):
    Advance to GO
    Go to JAIL
    Go to C1
    Go to E3
    Go to H2
    Go to R1
    Go to next R (railway company)
    Go to next R
    Go to next U (utility company)
    Go back 3 squares.

    The heart of this problem concerns the likelihood of visiting a particular square. That is,
    the probability of finishing at that square after a roll. For this reason it should be clear
    that, with the exception of G2J for which the probability of finishing on it is zero, the CH
    squares will have the lowest probabilities, as 5/8 request a movement to another square, and
    it is the final square that the player finishes at on each roll that we are interested in. We
    shall make no distinction between "Just Visiting" and being sent to JAIL, and we shall also
    ignore the rule about requiring a double to "get out of jail", assuming that they pay to get
    out on their next turn.

    By starting at GO and numbering the squares sequentially from 00 to 39 we can concatenate these
    two-digit numbers to produce strings that correspond with sets of squares.

    Statistically it can be shown that the three most popular squares, in order, are
    JAIL (6.24%) = Square 10, E3 (3.18%) = Square 24, and GO (3.09%) = Square 00.
    So these three most popular squares can be listed with the six-digit modal string: 102400.

    If, instead of using two 6-sided dice, two 4-sided dice are used, find the six-digit modal string.
"""
import random
import time
t0 = time.time()

with open("084.txt") as f:
    entries = f.read().splitlines()

class square():
    """instance of square in Monopoly"""
    def __init__(self, number, name):
        self.number = number
        self.name = name
        self.action = False
        self.n = 0
        # if you need to do anything when landing on the square
        if any(key in self.name for key in ["CH", "CC", "G2J"]):
            self.action = True

    def __repr__(self):
        return str(self.number) + ' ' + self.name + ' ' + str(self.action)

class state():
    """holds all the information for a state"""
    def __init__(self, position, ndoubles):
        self.position = position
        self.doubles = ndoubles
        self.jailtriples = 0

    def __repr__(self):
        return str(self.position) + ' ' + str(self.ndoubles)

squares = []
for i in range(len(entries)):
    squares.append(square(i, entries[i]))
ch = list(range(16))
cc = list(range(16))
random.shuffle(ch)
random.shuffle(cc)

def diceroll():
    sides = 4
    roll1 = random.randrange(1,sides + 1)
    roll2 = random.randrange(1,sides + 1)
    double = False
    if roll1 == roll2:
        double = True
    return (roll1 + roll2), double
def takeaturn(currentstate, squares, ch, cc):
    """ return newstate, squares, ch, cc after turn """
    newstate = currentstate
    roll, double = diceroll()
    # print("roll", roll)
    newstate.position = (newstate.position + roll) % 40
    # print(squares[newstate.position].name)

    # Sends to JAIL if third consecutive double
    if double:
        newstate.doubles += 1
        if newstate.doubles == 3:
            newstate.doubles = 0
            newstate.position = 10 # JAIL
            squares[newstate.position].n += 1
            newstate.jailtriples += 1
            return newstate, squares, ch, cc
    else:
        newstate.doubles = 0

    didmypositionupdate = True
    # CH, CC, G2J might require the position to be updated again
    while squares[newstate.position].action and didmypositionupdate:
        if "CH" in squares[newstate.position].name:
            ch, newstate, didmypositionupdate = drawchancecard(ch, newstate, squares)
        elif "CC" in squares[newstate.position].name:
            cc, newstate, didmypositionupdate = drawcommunitychestcard(cc, newstate)
        elif "G2J" == squares[newstate.position].name:
            newstate.position = 10
            didmypositionupdate = False
            # I know the position did update, but JAIL dosn't do anything so we just stay there.

    squares[newstate.position].n += 1
    return newstate, squares, ch, cc
def placecardatbottomofdeck(deck):
    newdeck = deck[1:]
    newdeck.append(deck[0])
    return newdeck
def positionofnext(RorU, position, squares):
    position += 1 # start searching from next position along
    if RorU == "railway":
        RorU = "R"
    elif RorU == "utility":
        RorU = "U"
    else:
        print("Error - can only search for next railway or utility")
        return None
    while True:
        if RorU in squares[position].name:
            return position
        position = (position + 1) % 40
def drawchancecard(ch, currentstate, squares):
    """
        0. Advance to GO    00
        1. Go to JAIL       10
        2. Go to C1         11
        3. Go to E3         24
        4. Go to H2         39
        5. Go to R1         05
        6. Go to next R (railway company)
        7. Go to next R
        8. Go to next U (utility company)
        9. Go back 3 squares.
    """
    newstate = currentstate
    didmypositionupdate = False
    if ch[0] == 0:
        newstate.position = 0
        didmypositionupdate = True
    elif ch[0] == 1:
        newstate.position = 10
        didmypositionupdate = True
    elif ch[0] == 2:
        newstate.position = 11
        didmypositionupdate = True
    elif ch[0] == 3:
        newstate.position = 24
        didmypositionupdate = True
    elif ch[0] == 4:
        newstate.position = 39
        didmypositionupdate = True
    elif ch[0] == 5:
        newstate.position = 5
        didmypositionupdate = True
    elif ch[0] == 6:
        newstate.position = positionofnext("railway", currentstate.position, squares)
        didmypositionupdate = True
    elif ch[0] == 7:
        newstate.position = positionofnext("railway", currentstate.position, squares)
        didmypositionupdate = True
    elif ch[0] == 8:
        newstate.position = positionofnext("utility", currentstate.position, squares)
        didmypositionupdate = True
    elif ch[0] == 9:
        newstate.position = (currentstate.position - 3) % 40
        didmypositionupdate = True
    else:
        pass
    ch = placecardatbottomofdeck(ch)
    return ch, newstate, didmypositionupdate
def drawcommunitychestcard(cc, currentstate):
    """
        0. Advance to GO    00
        1. Go to JAIL       10
    """
    newstate = currentstate
    didmypositionupdate = False
    if ch[0] == 0:
        newstate.position = 0
        didmypositionupdate = True
    elif ch[0] == 1:
        newstate.position = 10
        didmypositionupdate = True
    else:
        pass

    cc = placecardatbottomofdeck(cc)
    return cc, newstate, didmypositionupdate
def numberturns(squares):
    sum = 0
    for square in squares:
        sum += square.n
    return sum

state = state(0, 0)

turnnumber = 10000000
for i in range(turnnumber):
    state, squares, ch, cc = takeaturn(state, squares, ch, cc)

tf = time.time()
print(tf-t0)

sortedsquares = sorted(squares, key = lambda square: square.n, reverse = True)


numberturns = numberturns(squares)
for square in sortedsquares:
    probability = (square.n / numberturns) * 100
    print(square.name, '\t', probability)
