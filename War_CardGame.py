'''
o deck é dividido em dois e cada jogador fica com 26 cartas.
Cada jogador sempre pega as cartas de cima do seu deck e joga.
O jogador que tiver a carta com maior número ganha e leva a carta do outro
Em caso de empate, cada jogador tira mais duas cartas e adiciona ao monte (Início de uma WAR)
Cada jogador escolhe mais uma carta e quem tiver o maior número leva todo o monte.

'''

import random
suits = ('Hearts','Diamonds','Clubs','Spades')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

# Class for each individual card of the game
class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit

# Class for the deck
class Deck:

    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                # create the Card Object
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

# Class for creating players and their decks
class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            # list of multiple Card objects
            self.all_cards.extend(new_cards)
        else:
            # for a single Card object
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} card(s)'


######### Game Logic

def war_game():
    # Beginning of the game
    print('Welcome to War, the Card Game!')

    # Player's names
    player1_name = input("Please insert Player 1's name: ")
    player2_name = input("Please insert Player 2's name: ")
    print('\n\n')

    player1 = Player(player1_name)
    player2 = Player(player2_name)

    new_deck = Deck()
    new_deck.shuffle()

    # Constructing each player's deck
    # It basically distributes one card for each player alternating them
    builder = 1

    for each in range(1,53):
        if builder == 1:
            new_card = new_deck.deal_one()
            player1.add_cards(new_card)
            builder = 2
        else:
            new_card = new_deck.deal_one()
            player2.add_cards(new_card)
            builder = 1

    # Battle
    # Each player takes one card from the top of their deck

    while len(player1.all_cards) > 0 and len(player2.all_cards) > 0:
        battle_cards = [player1.remove_one(),player2.remove_one()]
        i = 0
        j = 1
        print(f'Player 1 plays {battle_cards[i]}')
        print(f'Player 2 plays {battle_cards[j]}')

        #Cards are compared to check who won the battle
        if battle_cards[i].value > battle_cards[j].value: # Player 1 wins and collects all cards
            print('Player 1 wins battle!')
            player1.add_cards(battle_cards)
            battle_cards.clear()
            print(player1)
            print(player2)
            print('\n\n')
        elif battle_cards[i].value < battle_cards[j].value: # Player 2 wins and collects all cards
            print('Player 2 wins battle!')
            player2.add_cards(battle_cards)
            battle_cards.clear()
            print(player1)
            print(player2)
            print('\n\n')
        elif battle_cards[i].value == battle_cards[j].value: # In case of a tie, a WAR starts
            print("It's a tie! Time for WAR!\n")
            # In case of a tie, each player picks +2 cards and battle for the total amount in the pile
            # (6 in the mount + 2 from new battle)
            # If a player does not have enough cards for a WAR, they lose the game
            if len(player1.all_cards) < 3:
                print('Player 1 does not have enough cards to continue.')
                print('Player 2 wins the game!')
                break
            elif len(player2.all_cards) < 3:
                print('Player 2 does not have enough cards to continue.')
                print('Player 1 wins the game!')
                break
            else:
                while True:
                    i += 6
                    j += 6
                    # Remove 2 cards from each player
                    for each in range(0,3):
                        battle_cards.append(player1.remove_one())
                        battle_cards.append(player2.remove_one())

                    print(f'Player 1 plays {battle_cards[i]}')
                    print(f'Player 2 plays {battle_cards[j]}')

                    # Battle for the pile of cards
                    if battle_cards[i].value > battle_cards[j].value:
                        print('Player 1 wins WAR!')
                        player1.add_cards(battle_cards)
                        battle_cards.clear()
                        print(player1)
                        print(player2)
                        print('\n\n')
                        break
                    elif battle_cards[i].value < battle_cards[j].value:
                        print('Player 2 wins WAR!')
                        player2.add_cards(battle_cards)
                        battle_cards.clear()
                        print(player1)
                        print(player2)
                        print('\n\n')
                        break

        # Reaching 0 cards
        if len(player1.all_cards) == 0:
            print('Player 2 wins the game!')
        elif len(player2.all_cards) == 0:
            print('Player 1 wins the game!')

war_game()