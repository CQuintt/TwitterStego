import string 

def main():

	well_constructed_tweets = []

	with open("words.txt") as f:
		dictionary = f.read().splitlines()

	with open("All_Tweets.txt") as f:
		lines = f.read().splitlines()
	lines = list(filter(None, lines))

	print("Starting...")
	for line in lines:
		flag = True
		words = line.split()
		if "@" in words[0]:
			for i in range(1,len(words)):
				if words[i] not in dictionary:
					#print("Bad Tweet")
					flag = False
					break
		else:
			for i in range(0,len(words)):
				if words[i] not in dictionary:
					#print("Bad Tweet")
					flag = False
					break	
		if flag == True:
			#print("Good Tweet")
			well_constructed_tweets.append(line)	

	data = '\n'.join(well_constructed_tweets)
	file = open("Well_Constructed_Tweets.txt", 'w')
	file.write(data)
	file.close()

main()