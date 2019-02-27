def createTrainingData(seq, vocab_size):

	num.set_printoptions(threshold=num.inf)
	seq_length = 2

	

	X = num.zeros((len(seq), seq_length, vocab_size), dtype=num.bool)
	y = num.zeros((len(seq), vocab_size), dtype=num.bool)

	for i,wordList in enumerate(seq):
		for j, word in enumerate(wordList):
			X[i,j,word] = 1

	for i in range(1,len(seq)):
		y[i-1,seq[i][1]] = 1


	model = createModel(seq_length, vocab_size)

	buildModel(model,X,y)