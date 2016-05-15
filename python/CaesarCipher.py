"""
	This class when given a string will return 
	return a uppercase string with each letter
	shifted by a given number
"""

class CaesarCipher(object):
	"""

	"""
	# Creating a dictionary where
	abc_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
	"N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
	abc_dict = {}
	for i,j in enumerate(abc_list, start=1):
		abc_dict[j] = i

	def __init__(self, shift):
		self.shift = int(shift)
		self.encoded_list = []
		self.decoded_list = []
		self.return_encoded = ""
		self.return_decoded = ""
        
	def encode(self, str_arg):
		for letter in str_arg.upper():
			num = CaesarCipher.abc_dict[letter]
			# ENCODE - Add the shift value 
			num += self.shift
			if num > 26:
				num -= 26
			self.encoded_list.append(num)
		# print CaesarCipher.abc_dict[letter]
		# print self.encoded_list
		for num in self.encoded_list:
			self.return_encoded += [letter for letter, number in CaesarCipher.abc_dict.items() if number == num][0]
		# self.decoded_list = [letter for num in self.encoded_list if  ]
		return self.return_encoded

	def decode(self, str_arg):
		for letter in str_arg.upper():
			num = CaesarCipher.abc_dict[letter]
			# DECODE - subtract the shift value
			num -= self.shift
			if num < 1:
				num += 26
			self.decoded_list.append(num)

		for num in self.decoded_list:
			self.return_decoded += [letter for letter, number in CaesarCipher.abc_dict.items() if number == num][0]
		return self.return_decoded

## testing ###
c = CaesarCipher(5); # creates a CipherHelper with a shift of five
print c.encode('Codewars') # returns 'HTIJBFWX'
print c.decode('BFKKQJX') # returns 'WAFFLES'
# [3, 15, 4, 5, 23, 1, 18, 19]
