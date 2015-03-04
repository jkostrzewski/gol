import copy

class RulesManager:
	rules = []

	def __init__(self):
		#rules.append(self.rule_1)
		return None


	def apply(self, world):
		new_world = world.world
		world_fields = copy.deepcopy(world.world)
		for i in range(world.height):
			for j in range(world.width):

				neighbours = self.count_neighbours(world, i, j)
				new_world[i][j] = self.rule_1(world_fields[i][j], neighbours)
				new_world[i][j] = self.rule_2(world_fields[i][j], neighbours)
		return new_world

	def rule_1(self, cell, neighbours):
		if cell.is_alive is False:
			if neighbours[0] == 3:
				cell.is_alive = True
			else:
				cell.is_alive = False
		return cell

	def rule_2(self, cell, neighbours):
		if cell.is_alive is True:
			if neighbours[0] == 3 or neighbours[0] == 2:
				cell.is_alive = True
			else:
				cell.is_alive = False
		return cell

	def count_neighbours(self, world, i, j):
		result = [0, 0, 0]
		for x in range(-1, 2):
			for y in range(-1, 2):
				if x == 0 and y == 0:
					continue
				try:
					if (i+x) >=0 and (j+y) >=0:
					#print i+x, j+y, str(world.world[i+x][j+y].is_alive)
						if world.world[i+x][j+y].is_alive is True:
							result[0] += 1
						else:
							result[1] += 1
					else:
						raise IndexError
				except IndexError:
					result[2]+=1
					
		print result, i, j
		return result

