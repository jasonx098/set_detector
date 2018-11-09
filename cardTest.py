from card import *

if __name__ == "__main__":
	card1 = CardRep(Shape(1), Color(1), Number(1), Shade(1))
	card2 = CardRep(Shape(1), Color(2), Number(0), Shade(1))
	cardeq = CardRep(Shape(1), Color(1), Number(1), Shade(1))
	cardList = set([cardeq])

	newCard = card1.makeSet(card2)
	print(newCard) # diamond orange three lines
	print(card1 == cardeq)
	print(card1 in cardList)
