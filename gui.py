import tkinter as tk
import nltk
from Hiaku import steg as s
from Hiaku import wordmap as wm
from Hiaku import haiku as h
import random

mappings = wm.Wordmap()
wordMap = mappings.populateMap()
grammar = nltk.data.load("grammar.txt",'cfg')

#DOES NOT WORK PROPERLY WITH SPACES FIX LATER
def printHaiku(path):
	syllables = []
	line1 = ""
	line2 = ""
	line3 = ""
	for terminal in path:
		syl = terminal.split("-")
		syllables.append(int(syl[0]))
	if (syllables[0] + syllables[1]) == 5:
		line1 = line1 + path[0] + path[1]

		if(syllables[2] + syllables[3] + syllables[4]) == 7:
			line2 = line2 + path[2] + " " + path[3] + " " + path[4]
			line3 = line3 + path[5] + " " + path[6] + " " + path[7]
		else:
			line2 = line2 + path[2] + " " + path[3] + " " + path[4] + " " + path[5]
			line3 = line3 + path[6] + " " + path[7]

	elif (syllables[0] + syllables[1] + syllables[2]) == 5:
		line1 = line1 + path[0] + " " + path[1] + " " + path[2]
		line2 = line2 + path[3] + " " + path[4] + " " + path[5]
		line3 = line3 + path[6] + " " + path[7]
	
	haikuLine1["text"] = line1
	haikuLine2["text"] = line2
	haikuLine3["text"] = line3

def buildHaiku(rules, wordDictionary): # TODO: ADD MANUAL USER ASSIGNMENT 
	""" Construct a haiku from the production rules provided and dictionary of terminal words"""
	haiku = []
	for terminal in rules:
		selection = []
		flag = True
		# get a selection of random words from
		# the dictionary for that specfic terminal symbol
		#(TEMPORAY UNTIL RNN PREDICTION IS IMPLEMENTED)
		for i in range(0,50):
			pick = random.choice(wordDictionary[terminal])
			dropListBox.insert(i,pick)
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

def prepareData(message):
	hai = h.Haiku()
	stego = s.Steg()
	binaryArray = stego.binaryize(message)
	for code in binaryArray:
		paths = hai.getPaths(grammar, code)
		chosenPath = hai.randomPath(paths)
		printHaiku(chosenPath)
		buildHaiku(chosenPath, wordMap)


root = tk.Tk()

canvas = tk.Canvas(root, height = 500, width = 900)
canvas.pack()

background = tk.Frame(root, bg="#022c43")
background.place(x=0, y=0,relwidth=1,relheight=1)

############################################# HEADER #####################################
header = tk.Frame(root, bg="#115173")
header.place(relx=0.025, rely=0.025,relwidth=0.95,relheight=0.1)

nameLabel = tk.Label(header,text="HaiSteg", bg="#115173",fg="#ffd700", font=("Helvetica", 28))
nameLabel.place(relx=0.025, rely=0)
searchLabel = tk.Label(header,text="Search", bg="#115173",fg="#fff", font=("Helvetica", 16))
searchLabel.place(relx=0.2, rely=0.225)
hideLabel = tk.Label(header,text="Hide Text", bg="#115173",fg="#fff", font=("Helvetica", 16))
hideLabel.place(relx=0.3, rely=0.225)

############################################# SEARCH BAR #####################################
searchFrame = tk.Frame(root, bg="#115173")
searchFrame.place(relx=0.025, rely=0.15,relwidth=0.95,relheight=0.1)

entry = tk.Entry(searchFrame,bg="#fff")
entry.place(relx="0.025", rely="0.2", relwidth="0.6", relheight="0.6")
secretButton = tk.Button(searchFrame,bg="#ffd700", text="Encode Secret Message", command=lambda:prepareData(entry.get()))
secretButton.place(relx="0.65",rely="0.2", relwidth="0.325", relheight="0.6")

############################################# HAIKU CONTAINER #####################################
haikuFrame = tk.Frame(root, bg="#115173")
haikuFrame.place(relx=0.025, rely=0.275,relwidth=0.5,relheight=0.7)

haikuLine1 = tk.Label(haikuFrame, bg="#115173",fg="#fff", font=("Helvetica", 18))
haikuLine1.place(relx=0.2, rely=0.275, relwidth=0.6, relheight=0.15)
haikuLine2 = tk.Label(haikuFrame, bg="#115173",fg="#fff", font=("Helvetica", 18))
haikuLine2.place(relx=0.2, rely=0.425, relwidth=0.6, relheight=0.15)
haikuLine3 = tk.Label(haikuFrame, bg="#115173",fg="#fff", font=("Helvetica", 18))
haikuLine3.place(relx=0.2, rely=0.575, relwidth=0.6, relheight=0.15)

############################################# POS CONTAINER #####################################
posFrame = tk.Frame(root, bg="#115173")
posFrame.place(relx=0.550, rely=0.275,relwidth=0.425,relheight=0.1)

############################################# DROPDOWN CONTAINER #####################################
dropDownFrame = tk.Frame(root, bg="#115173")
dropDownFrame.place(relx=0.550, rely=0.425,relwidth=0.2,relheight=0.35)

dropDownLabel = tk.Label(dropDownFrame,text="Select a word", bg="#115173",fg="#ffd700", font=("Helvetica", 14))
dropDownLabel.place(relx=0.15, rely=0.025)
dropListBox = tk.Listbox(dropDownFrame)
dropListBox.place(relx="0.075", rely="0.275", relwidth="0.85", relheight="0.6")

selectWordButton = tk.Button(root,bg="#ffd700", text="Select Word", font=("Helvetica", 16))
selectWordButton.place(relx="0.550",rely="0.8", relwidth="0.2", relheight="0.175")

############################################# MANUAL ENTRY CONTAINER #####################################
manualFrame = tk.Frame(root, bg="#115173")
manualFrame.place(relx=0.775, rely=0.425,relwidth=0.2,relheight=0.35)

manualLabel = tk.Label(manualFrame,text="Manual Input", bg="#115173",fg="#ffd700", font=("Helvetica", 14))
manualLabel.place(relx=0.175, rely=0.025)
manualEntry = tk.Entry(manualFrame,bg="#fff")
manualEntry.place(relx="0.075", rely="0.325", relwidth="0.85", relheight="0.2")

enterWordButton = tk.Button(root,bg="#ffd700", text="Enter Word", font=("Helvetica", 16))
enterWordButton.place(relx="0.775",rely="0.8", relwidth="0.2", relheight="0.175")

root.mainloop()