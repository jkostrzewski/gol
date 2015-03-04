from cell import Cell
from rules_manager import RulesManager
import os
import copy

class World:
	width = 50
	height = 50
	world = [[]]
	seed_ratio = 0.1
	rules = []
	rules_manager = RulesManager()

	def initialize(self):
		world = []
		for i in range(self.height):
			world.append([Cell().randomize(self.seed_ratio) for j in range(self.width)])
		self.world = world

	def draw(self):
		os.system('clear')
		print('\n'.join([''.join(['{:2}'.format(item) for item in row]) for row in self.world]))

	def next_generation(self):
		new = copy.deepcopy(self.rules_manager.apply(self))
		self.world = new


