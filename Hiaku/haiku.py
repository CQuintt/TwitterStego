from nltk.corpus import wordnet as wn
from nltk import CFG
from nltk.parse.generate import generate, demo_grammar
from nltk.parse import RecursiveDescentParser
import nltk
import random
import string
import binascii

class Haiku(object):

	def randomPath(self,paths):
		print(paths)
		pick = random.choice(paths)
		print(pick)
		return pick

	def getPaths(self,grammar, binarySequence):
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
	
	def buildHaiku(self,rules, wordDictionary): # TODO: ADD MANUAL USER ASSIGNMENT 
		""" Construct a haiku from the production rules provided and dictionary of terminal words"""
		haiku = []
		for terminal in rules:
			selection = []
			flag = True
			# get a selection of random words from
			# the dictionary for that specfic terminal symbol
			#(TEMPORAY UNTIL RNN PREDICTION IS IMPLEMENTED)
			for i in range(0,20):
				pick = random.choice(wordDictionary[terminal])
				selection.append(pick)
			print(selection)
			#loop until user selects a word located in selection array
			while(flag):
				wordChoice = input("\n Select a word: \n")
				if wordChoice in selection:
					haiku.append(wordChoice)
					#break loop and move onto next rule
					flag = False
				else:
					print("Invalid word")
		return haiku