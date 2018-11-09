from solver import setSolver
from card import *

if __name__ == "__main__":
	sample = []
	sample.append(CardRep(Shape(0), Color(0), Number(0), Shade(0)))
	sample.append(CardRep(Shape(2), Color(2), Number(2), Shade(2)))
	sample.append(CardRep(Shape(1), Color(1), Number(1), Shade(1)))

	sample.append(CardRep(Shape(2), Color(1), Number(1), Shade(0)))
	sample.append(CardRep(Shape(0), Color(0), Number(2), Shade(2)))
	sample.append(CardRep(Shape(1), Color(2), Number(0), Shade(1)))

	sample.append(CardRep(Shape(1), Color(0), Number(2), Shade(2)))
	sample.append(CardRep(Shape(0), Color(1), Number(0), Shade(2)))
	sample.append(CardRep(Shape(2), Color(2), Number(1), Shade(2)))

	retTup = setSolver(sample)

	if retTup[0]:
		for sol in retTup[1]:
			print(sol)





