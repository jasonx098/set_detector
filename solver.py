from card import *
from itertools import combinations

# return a tuple (boolean, list)
def setSolver(cardList):
	ret = setList(cardList)
	if len(ret) == 0:
		return (False, ret)
	return (True, ret)

# input: python list of cards
# output: a list of valid set tuples
def setList(cardList):
	#cardSet = set(cardList)
	cardRetList = []
	#for i in cardSet: print(i)
	#print(cardSet)

	# iterate through all n^2 combinations
	for com in combinations(cardList, 2):
		validSetRet = validSet(com[0], com[1], cardList)
		if validSetRet[0]:
			cardRetList.append((com[0], com[1], validSetRet[1]))

	return cardRetList

# input: two cards and the set of cards
# output: returns a tuple of (True, card) if valid
def validSet(card1, card2, cardList):
	newCard = card1.makeSet(card2)
	if newCard in cardList:
		return (True, newCard)
	return (False, None)








