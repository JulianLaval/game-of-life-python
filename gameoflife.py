#! python3

from os import system, name
from sys import stdin
from copy import deepcopy
from html import parser

# input = stdin.read().splitlines()
f = open("input.txt")
input = f.read().splitlines()

global inputArray
inputArray = []	
for line in input:
	inputArray.append(list(line))
	
def nextGen(inputArray):
	newArray = deepcopy(inputArray)
	for lineKey, line in enumerate(inputArray):
		for charKey, char in enumerate(line):
			if inputArray[lineKey][charKey] == "1" and neighbours(lineKey, charKey) < 2:
				newArray[lineKey][charKey] = "0"
			elif inputArray[lineKey][charKey] == "1" and neighbours(lineKey, charKey) > 3:
				newArray[lineKey][charKey] = "0"
			elif inputArray[lineKey][charKey] == "0" and neighbours(lineKey, charKey) == 3:
				newArray[lineKey][charKey] = "1"
	return newArray

def neighbours(y, x):
	counter = 0
	try:
		if x-1 >= 0 and y-1 >= 0 and inputArray[y-1][x-1] == "1":
			counter += 1
	except:
		pass
	try:
		if x >= 0 and y-1 >= 0 and inputArray[y-1][x] == "1":
			counter += 1
	except:
		pass
	try:
		if x+1 >= 0 and y-1 >= 0 and inputArray[y-1][x+1] == "1":
			counter += 1
	except:
		pass
	try:
		if x-1 >= 0 and y >= 0 and inputArray[y][x-1] == "1":
			counter += 1
	except:
		pass
	try:
		if x+1 >= 0 and y >= 0 and inputArray[y][x+1] == "1":
			counter += 1
	except:
		pass
	try:
		if x-1 >= 0 and y+1 >= 0 and inputArray[y+1][x-1] == "1":
			counter += 1
	except:
		pass
	try:
		if x >= 0 and y+1 >= 0 and inputArray[y+1][x] == "1":
			counter += 1
	except:
		pass
	try:
		if x+1 >= 0 and y+1 >= 0 and inputArray[y+1][x+1] == "1":
			counter += 1
	except:
		pass
	return counter

decode = parser.HTMLParser()
# decode.unescape('&#9608;') FULL BLOCK
# decode.unescape('&#9617;') LIGHT SHADE

gen = 0
while True:
	newPrint = deepcopy(inputArray)
	for lineKey, line in enumerate(inputArray):
		for charKey, char in enumerate(line):
			if char == "1":
				newPrint[lineKey][charKey] = decode.unescape('&#9608;')
			elif char == "0":
				newPrint[lineKey][charKey] = decode.unescape('&#9617;')
	print("Generation: ",str(gen),"\n\n")
	print( '\n'.join([''.join(line) for line in newPrint]))
	gen+=1
	inputArray = nextGen(inputArray)
	system("pause")
	system('cls' if name=='nt' else 'clear')