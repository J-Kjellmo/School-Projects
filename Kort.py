import random as rd
import os

class Kortstokk:
    def __init__(self):
        self.deck = [f'{suit}{rank}' for suit in ["H", "D", "C", "S"] for rank in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]]
        rd.shuffle(self.deck)
        self.hands = {}
        self.handIdentifiers = {}
        
    def hand(self, n):
        handTemporary = []
        for i in range(n):
            handTemporary.append(self.deck[0])
            self.deck.pop(0)
        return handTemporary

    def dealOut(self, p):
        for i in range(p):
            playerName = input(f'insert username for player {i + 1}: ')
            currentHand = Kort.hand(5)
            self.hands[playerName] = currentHand
            self.handIdentifiers[f'p{i+1}'] = playerName

    def __str__(self):
        return ' '.join(map(str, self.deck))

class Olsen:
    def __init__(self):
        self.deck = Kort.deck
        self.hands = Kort.hands
        self.handIdentifiers = Kort.handIdentifiers
        self.redBlack = {'red': ['H', 'D'], 'black': ['C', 'S']}

    def runde(self):
        rotation = 0
        drawn = 0
        topCard = ''
        while True:
            drew = False
            os.system('cls')
            rotation += 1
            if rotation > len(self.hands):
                rotation = 1

            if drawn < 3:    
                if self.deck[0][0] in self.redBlack['red']:
                    topCard = 'red'
                else:
                    topCard = 'black'

                print(f'top kortet er: {self.deck[0]}')
                print(self.handIdentifiers[f'p{rotation}'], 'sin tur!')
                print(' '.join(map(str, self.hands[self.handIdentifiers[f'p{rotation}']])))

                while True:
                    currentMove = input('(Type help for help) What is your move?: ')

                    if currentMove in self.hands[self.handIdentifiers[f'p{rotation}']] and currentMove[0] in self.redBlack[f'{topCard}'] or currentMove[1] == self.deck[0][1] or currentMove[1] == '8': # if statement som sjekker om kortet som spilleren prøver å legge på er valid
                        self.hands[self.handIdentifiers[f'p{rotation}']].remove(f'{currentMove}')
                        self.deck.insert(0, f'{currentMove}')
                        drawn = 0
                        break

                    if currentMove == 'draw':
                        self.hands[self.handIdentifiers[f'p{rotation}']].append(self.deck[-1])
                        self.deck.pop(-1)
                        drew = True
                        drawn += 1
                        break
                    
                    if currentMove == 'help':
                        Olsen.help()

                    print('Move is invalid! Try again. (type help for help)\n')

            else:
                drawn = 0

            if len(self.hands[self.handIdentifiers[f'p{rotation}']]) <= 0:
                os.system('cls')
                print(self.handIdentifiers[f'p{rotation}'], 'vinner!')
                break

            if drew == True: #
                rotation -= 1

    def help():
        print('If you enter an input and another input prompt appears, it means that your input is invalid')
        print('if you do not have a card to lay out, then you have to draw until you have a card the you can lay out, or until you have drawn in 3 card')
        print('to draw a card, type out: "draw"')
        print('To lay down a card, type the card out like this: "H4"\n')




Kort = Kortstokk()
olsenSpill = Olsen()

while True:
    try:
        handsAmount = int(input('How many players?: '))
    except:
        pass
    else:
        if handsAmount > 1 and handsAmount <= 6:
            break

Kort.dealOut(handsAmount)

olsenSpill.runde()