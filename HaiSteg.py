import nltk
from Hiaku import haiku as h
from Hiaku import Bot as b
from Hiaku import steg as s
from Hiaku import wordmap as wm
import random

API_key = "u1NpPWoQ0klxIE1tnEfeeKfLa"
API_secret_key = "XxFJecfOJtnG4WdLgMAvGPNkyEmSavw8tPfIExR8VCURGV4Rbn"
access_token = "1088648194555289600-weVaU8a1hTZ8st6zUfVaQvfiL8L09M"
access_token_secret = "afKljvXSZzyBHwHDsgwCGE6BdBSuq2K2qRuK5Js92vjLy"

def randomPath(paths):
	print(paths)
	pick = random.choice(paths)
	print(pick)
	return pick
	

def getPaths(grammar, binarySequence):
	paths = []
	parser =  nltk.ChartParser(grammar)
	for tree in parser.parse(binarySequence):
		path = []
		for branch in tree:
			for leaf in branch:
				token = str(leaf)
				token = token.strip("()")
				token = token.split(" ")
				#check if 7 syllable line expands the 5-SYL Non-Terminal (this will count as anothewr branch)
				if "5-SYL" in token:
					#if so expand that branch and add containing tokens to path, discard Non-Terminal
					for subLeaf in leaf:
						token = str(subLeaf)
						token = token.strip("()")
						token = token.split(" ")
						path.append(token[0])
				else:
					path.append(token[0])
		paths.append(path)
	return paths


def main():
	#initialise classes
	hai = h.Haiku()
	twitterBot = b.Bot(API_key,API_secret_key, access_token, access_token_secret)
	stego = s.Steg()
	mappings = wm.Wordmap()
	wordMap = mappings.populateMap()
	grammar = nltk.data.load("grammar.txt",'cfg')

	secret_message = input("Enter a secret message! \n")
	binaryArray = stego.binaryize(secret_message)
	print(binaryArray)
	for code in binaryArray:
		paths = getPaths(grammar, code)
		chosenPath = randomPath(paths)
		hai.buildHaiku(chosenPath, wordMap)

main()