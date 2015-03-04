from cell import Cell
from rules_manager import RulesManager
import os
import copy

class World:
	width = 200
	height = 130
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
		self.world = self.rules_manager.apply(self)
		


	def copy(self):
		w = World()
		w.initialize()
		for i in range(self.height):
			for j in range(self.width):
				w.world[i][j] = self.world[i][j].copy()
		return w
