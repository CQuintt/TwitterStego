import tensorflow as tf 
import keras as ker
import numpy as num
import os
import string
import sys
from pickle import dump

# load doc into memory
def load_doc(filename):
	# open the file as read only
	file = open(filename, 'r', encoding="ISO-8859-1")
	# read all text
	text = file.read()
	# close the file
	file.close()
	return text
 
# turn a doc into clean tokens
def clean_doc(doc):

	# split into tokens by white space
	tokens = doc.split()
	# remove punctuation from each token
	tokens = [word.translate(string.punctuation) for word in tokens]
	# remove remaining tokens that are not alphabetic
	tokens = [word for word in tokens if word.isalpha()]
	# make lower case
	tokens = [word.lower() for word in tokens]
	return tokens
 
# save tokens to file, one dialog per line
def save_doc(lines, filename):
	data = '\n'.join(lines)
	file = open(filename, 'w')
	file.write(data)
	file.close()

def createSequences(tokens):

	#Create sequences of tokens
	length = 2
	sequence_list = list()

	for i in range(length, len(tokens)):
		sequences = tokens[i - length : i]
		sentence = " ".join(sequences)
		sequence_list.append(sentence)
	print(len(sequence_list))

	return sequence_list

def tokenizeWords(file):
	
	lines = file.split("\n")
	tokenizer = ker.preprocessing.text.Tokenizer()
	tokenizer.fit_on_texts(lines)
	seq = tokenizer.texts_to_sequences(lines)

	vocab_size = len(tokenizer.word_index) + 1

	#print(seq)

	# save the tokenizer
	dump(tokenizer, open('tokenizer3.pkl', 'wb'))

	createTrainingData(seq, vocab_size)


def saveModel(model):

	# save the model to file
	model.save('model3.h5')


def buildModel(model,X,y):

	# compile model
	model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
	# fit model
	model.fit(X, y, batch_size=250, epochs=300)

	saveModel(model)

def createModel(seq_length, vocab_size):

	model = ker.Sequential()
	model.add(ker.layers.Embedding(vocab_size, 50, input_length=seq_length))
	model.add(ker.layers.LSTM(100, return_sequences=True))
	model.add(ker.layers.LSTM(100))
	model.add(ker.layers.Dense(100, activation='relu'))
	model.add(ker.layers.Dense(vocab_size, activation='softmax'))
	print(model.summary())

	return model

def createTrainingData(seq, vocab_size):

	num.set_printoptions(threshold=num.inf)
	seq_length = 2

	sequences = num.array(seq)
	X, y = sequences[:,:-1], sequences[:,-1]
	y = ker.utils.to_categorical(y, num_classes=vocab_size)
	seq_length = X.shape[1]


	model = createModel(seq_length, vocab_size)

	buildModel(model,X,y)

def main():

	# load document
	#stores the file name provided via user input
	in_filename = input("Please enter a training file: ")
	doc = load_doc(in_filename)
	 
	# clean document
	tokens = clean_doc(doc)
	print('Total Tokens: %d' % len(tokens))
	print('Unique Tokens: %d' % len(set(tokens)))
 
	sequences = createSequences(tokens)

	save_doc(sequences,"training_sequences3.txt")
	doc = load_doc("training_sequences3.txt")

	tokenizeWords(doc)


main()