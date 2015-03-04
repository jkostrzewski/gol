#!/usr/bin/env python

from src.world import World
from src.visualizer import Visualizer
import time

def main():
	world = World()
	world.initialize()
	vis = Visualizer(world = world)
	print 'asd'
	while True:
		print 'asd'
		world.next_generation()
		vis.update_data(world)  



if __name__ == '__main__':
	main()