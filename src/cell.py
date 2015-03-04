import random

class Cell:

	is_alive =  False


	def randomize(self, ratio):
		if random.random() < ratio:
			self.is_alive = True
		else:
			self.is_alive = False
		return self

	def make_alive(self):
		self.is_alive = True

	def make_dead(self):
		self.is_alive = False

	def __str__(self):
		if self.is_alive is True:
			return '@'
		else:
			return ' '