
class Steg(object):

	def binaryize(self,message):
		"""convert chars in a message to their equivillent binary value"""
		dataArray = []
		for char in message:
			binaryString ="0"
			binaryData = format(ord(char), 'b')
			binaryString = binaryString + str(binaryData)
			dataArray.append(binaryString)

		return dataArray

	#def encode():


	#def decode():
