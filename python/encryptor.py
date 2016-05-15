"""
"""

def encryptor(key, message):
	abc_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
	abc_dict = {}
	for i,j in enumerate(abc_list, start=1):
		abc_dict[j] = i

	# print abc_dict

	# message list
	message_list = []
	# return string
	return_str = ""
	# create a for loop that gives you the number of each letter in the message
	for char in message:
		try:
			num = abc_dict[char.upper()]
			num += int(key)
			if num > 26:
				num = num % 27 + 1
			# elif num == 0:
			# 	num = 26
			elif num <1:
				num = 26 - (abs(num) % 27)

			message_list.append(num)
		except:
			message_list.append(char)
	# print message_list
	for num in message_list:
		# print num
		if type(num) == int:
			# print num
			return_str += next((letter for letter, number in abc_dict.items() if number == num), None)
			# print [key for key, value in abc_dict.items() if key == num]
			# return_str += [key for key, value in abc_dict.items() if key == num][0]
		else:
			return_str += num
	return return_str

	# 


			# for num in self.encoded_list:
			# if type(num) == int:
			# 	# print [letter for letter, number in CaesarCipher.abc_dict.items() if number == num][0]
			# 	self.return_encoded += [letter for letter, number in CaesarCipher.abc_dict.items() if number == num][0]
			# else:
			# 	self.return_encoded += num


			


####### testing
print encryptor(27, 'Whoopi Goldberg')
