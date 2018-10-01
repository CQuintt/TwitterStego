import sys

alphabet = {'a' : 1,
			"b" : 2,
			"c" : 3,
			"d" : 4,
			"e" : 5,
			"f" : 6,
			"g" : 7,
			"h" : 8,
			"i" : 9,
			"j" : 10,
			"k" : 11,
			"l" : 12,
			"m" : 13,
			"n" : 14,
			"o" : 15,
			"p" : 16,
			"q" : 17,
			"r" : 18,
			"s" : 19,
			"t" : 20,
			"u" : 21,
			"v" : 22,
			"w" : 23,
			"x" : 24,
			"y" : 25,
			"z" : 26,
			'A' : 1,
			"B" : 2,
			"C" : 3,
			"D" : 4,
			"E" : 5,
			"F" : 6,
			"G" : 7,
			"H" : 8,
			"I" : 9,
			"J" : 10,
			"K" : 11,
			"L" : 12,
			"M" : 13,
			"N" : 14,
			"O" : 15,
			"P" : 16,
			"Q" : 17,
			"R" : 18,
			"S" : 19,
			"T" : 20,
			"U" : 21,
			"V" : 22,
			"W" : 23,
			"X" : 24,
			"Y" : 25,
			"Z" : 26,
			"'" : 0,
			"-" : 0,
			"/"	: 0,
			"&"	: 0,
			"_" : 0,
			"." : 0,
			"!" : 0,
			"?" : 0,
			"1" : 0,
			"2" : 0,
			"3" : 0,
			"4" : 0,
			"5" : 0,
			"6" : 0,
			"7" : 0,
			"8" : 0,
			"9" : 0,
			"0" : 0,
			}
dictionary = {}

def getVal(x):
	value = 0
	for char in x:
		value+=alphabet[char]
	return value

def loadDictionary():
	with open("values.txt") as f:
		for line in f:
			contents = line.split()
			key = contents[0]
			val = contents[1]
			dictionary[key] = int(val)


def main():
	loadDictionary()
	x = raw_input("Enter a tweet: \n")
	wordVal = getVal(x)
	print(wordVal)
	for key, values in dictionary:
		if(dictionary[key] == wordVal):
			print(key)


if __name__ == '__main__':
	main()
