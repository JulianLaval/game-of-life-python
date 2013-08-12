# The Game of Life - Python

Conway's Game of Life, in Python 3.3!

## Instructions

Input pattern is read from a text file. The default file name is input.txt. To modify this, change the file name where indicated:

	# # # # # FILE INPUT # # # # #
	f = open("input.txt")
	# # # # # # # # # # # # # # #

In their initial configuration, must be represented by either 0 (dead) or 1 (alive). For example, a simple blinker should be inputted as follows:

	00000
	00000
	01110
	00000
	00000

One of the states of a 3 period pulsar would be:

	00000000000000000
	00000000000000000
	00001110001110000
	00000000000000000
	00100001010000100
	00100001010000100
	00100001010000100
	00001110001110000
	00000000000000000
	00001110001110000
	00100001010000100
	00100001010000100
	00100001010000100
	00000000000000000
	00001110001110000
	00000000000000000
	00000000000000000

To progress to the next generation, simply press any button.

##### Note: due to the finite nature of the map, live cells that reach the edge will stop progressing and might interfere with neighbouring cells.

## To-do

* Variable map sizes
* Option to create generations at automatic intervals
* Better simulate infinite size
