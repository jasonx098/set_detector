from enum import Enum 

class Shape(Enum):
	circle = 0
	diamond = 1
	squiggle = 2

class Color(Enum):
	orange = 0
	green = 1
	purple = 2

class Number(Enum):
	one = 0
	two = 1
	three = 2

class Shade(Enum):
	clear = 0
	lines = 1
	solid = 2

class CardRep:

	# typing as Shape, Color, Number, Shade
	def __init__(self, shap, colo, numb, shad):
		self.shap = shap
		self.colo = colo
		self.numb = numb
		self.shad = shad

	def __repr__(self):
		return (self.shap.name + " " + self.colo.name + " " + self.numb.name + " " + self.shad.name)

	def __eq__(self, card):
		return isinstance(card, CardRep) and card.shap == self.shap and card.colo == self.colo and card.numb == self.numb and card.shad == self.shad

	def __hash__(self):
		return id(self)

	def makeSet(self, card):
		newShap = (3 - self.shap.value - card.shap.value) % 3
		newColo = (3 - self.colo.value - card.colo.value) % 3
		newNumb = (3 - self.numb.value - card.numb.value) % 3
		newShad = (3 - self.shad.value - card.shad.value) % 3

		return CardRep(Shape(newShap), Color(newColo), Number(newNumb), Shade(newShad))










