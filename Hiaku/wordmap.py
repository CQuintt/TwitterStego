import os

class Wordmap(object):

	def populateMap(self):


		wordMappings = {
						"1-N" : "",
						"2-N" : "",
						"3-N" : "",
						"4-N" : "",

						"1-V" : "",
						"2-V" : "",
						"3-V" : "",
						"4-V" : "",
						"5-V" : "",
						"6-V" : "",

						"1-ADJ" : "",
						"2-ADJ" : "",
						"3-ADJ" : "",
						"4-ADJ" : "",

						"1-P"	: "",
						"2-P"	: "",

						"1-DET" : "",
						"1-AUX" : ""
		}

		script_dir = os.path.dirname(__file__)
		rel_path = "syllables/"
		file_path = os.path.join(script_dir,rel_path)

		with open(file_path + "nouns-1.txt") as f1:
			nouns = f1.read().split()
			wordMappings["1-N"] = nouns

		with open(file_path + "nouns-2.txt") as f2:
			nouns = f2.read().split()
			wordMappings["2-N"] = nouns

		with open(file_path + "nouns-3.txt") as f3:
			nouns = f3.read().split()
			wordMappings["3-N"] = nouns

		with open(file_path + "nouns-4.txt") as f4:
			nouns = f4.read().split()
			wordMappings["4-N"] = nouns

		###############################################################################################

		with open(file_path + "verbs-1.txt") as f5:
			verbs = f5.read().split()
			wordMappings["1-V"] = verbs

		with open(file_path + "verbs-2.txt") as f6:
			verbs = f6.read().split()
			wordMappings["2-V"] = verbs

		with open(file_path + "verbs-3.txt") as f7:
			verbs = f7.read().split()
			wordMappings["3-V"] = verbs

		with open(file_path + "verbs-4.txt") as f8:
			verbs = f8.read().split()
			wordMappings["4-V"] = verbs

		with open(file_path + "verbs-5.txt") as f9:
			verbs = f9.read().split()
			wordMappings["5-V"] = verbs

		with open(file_path + "verbs-6.txt") as f10:
			verbs = f10.read().split()
			wordMappings["6-V"] = verbs

		#####################################################################################################

		with open(file_path + "adj-1.txt") as f11:
			adj = f11.read().split()
			wordMappings["1-ADJ"] = adj

		with open(file_path + "adj-2.txt") as f12:
			adj = f12.read().split()
			wordMappings["2-ADJ"] = adj

		with open(file_path + "adj-3.txt") as f13:
			adj = f13.read().split()
			wordMappings["3-ADJ"] = adj

		with open(file_path + "adj-3.txt") as f14:
			adj = f14.read().split()
			wordMappings["4-ADJ"] = adj
		##############################################################################################

		with open(file_path + "pre-1.txt") as f15:
			pre = f15.read().split()
			wordMappings["1-P"] = pre

		with open(file_path + "pre-1.txt") as f16:
			pre = f16.read().split()
			wordMappings["2-P"] = pre

		###############################################################################################

		with open(file_path + "det-1.txt") as f17:
			det = f17.read().split()
			wordMappings["1-DET"] = det

		return wordMappings