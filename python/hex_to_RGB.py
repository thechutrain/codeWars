"""
	Practice Script - useful for solving a code war problem
"""

def hex_to_RGB(hex_str):
	"""
	This function will take one six-digit hex numbers
	and convert it to a three two-digit RGB coordinate 
	"""
	# dictionary constant for conversion
	hex_digit_dict = {
	"0": 0,
	"1": 1,
	"2": 2,
	"3": 3,
	"4": 4,
	"5": 5,
	"6": 6,
	"7": 7,
	"8": 8,
	"9": 9,
	"A": 10,
	"B": 11,
	"C": 12,
	"D": 13,
	"E": 14,
	"F": 15
	}

	#assume valid data - 6 letter string
	# hex_1 = hex_str[0:2]
	# hex_2 = hex_str[2:4]
	# hex_3 = hex_str[4:6]

	# calculate the RGB number
	def RGB_number(hex_num):
		num = (hex_digit_dict[hex_num[0]]* (16 **1)) + (hex_digit_dict[hex_num[1]]* (16**0))
		return num
	
	num_1 = RGB_number(hex_str[0:2])
	num_2 = RGB_number(hex_str[2:4])
	num_3 = RGB_number(hex_str[4:6])

	print "Your RGB number is: %r, %r, %r" % (num_1, num_2, num_3)

######## TESTING #########
hex_to_RGB("9400D3")