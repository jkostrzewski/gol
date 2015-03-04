#!/usr/bin/env python

from src.world import World
import time

def main():
	world = World()
	world.initialize()
	while True:
		world.draw()
		world.next_generation()
		raw_input()


if __name__ == '__main__':
	main()