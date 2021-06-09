"""
	Simulation of 2 bots playing color matching game with a set of cards. Each card has a color and a number
"""

import random
import time

class Card():
	"""
		Represents a playing card. 
		Card Colors: ["Red","Green","Blue","Yellow"]
		Each color has 10 cards ranging from 1 to 10
	"""

	def __init__(self, color,number):
		super(Card, self).__init__()
		self.color = color
		self.number = number
	
	def __str__(self):
		return str(self.number) + " of " + str(self.color)

card_colors = ["Red","Green","Blue","Yellow"]
card_numbers = [x for x in range(1,11)]


# Creates a random deck of N cards
def create_deck(N = 10):
	deck = []
	for i in range(N):
		deck.append(Card(random.choice(card_colors),random.choice(card_numbers)))

	return deck

def get_randomcard():
	return Card(random.choice(card_colors),random.choice(card_numbers))

def next_turn(piletop,deck):
	index = 0
	for card in deck:
		if piletop.color == card.color or piletop.number == card.number:
			deck.pop(index)
			return card,deck

		index += 1 

	# no card found, so add a random card to the deck
	card = get_randomcard()
	print("---------Picks a random card from heap---")
	if card.color != piletop.color and piletop.number != card.number:
		deck.append(card) # this skips turn for this player if matching color card not picked 
		card = False

	return card,deck


print("Starting game")
players = ["Player1","Player2"]
winner = "None"

# Create decks for both players
deckSize = 10
deck1 = create_deck(deckSize)
deck2 = create_deck(deckSize)
print([str(card) for card in deck1])
print([str(card) for card in deck2])
print("Decks loaded....\n")

# Play turns until one of the decks are finished. Each turn a player plays a same color card OR same number card as top of pile
pile = get_randomcard()
print("Initial Pile: " + str(pile) + "\n")

turn = 0
maxturns = 100
while len(deck1) > 0 and len(deck2) > 0 and turn <= maxturns:
	turn += 1

	time.sleep(1)
	print("_____________ TURN " + str(turn) + " ________________")

	card1,deck1 = next_turn(pile,deck1)
	if(card1):
		pile = card1
		print("P1 played " + str(card1))
	else:
		print("P1 skipped turn") 
	time.sleep(2)	
	card2,deck2 = next_turn(pile,deck2)
	if(card2):
		pile = card2
		print("P2 played " + str(card2))
	else:
		print("P2 skipped turn") 
	
	# check for winners
	if(len(deck1) == 0):
		print("P1 WON!")
		winner = players[0]
		break 
	elif(len(deck2) == 0):
		print("P2 WON!")
		winner = players[1]
		break 

print("\n\nGame finished. Winner: " + winner)