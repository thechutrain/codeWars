"""
	Codewars - 5 kyu
	The rgb() method is incomplete. Complete the method so that passing in RGB decimal values 
	will result in a hexadecimal representation being returned. The valid decimal values for 
	RGB are 0 - 255. Any (r,g,b) argument values that fall out of that range should be rounded
	 to the closest valid value. 
"""

def rgb(r,g,b):
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

	def get_hex(num):
		# hex_1 = num / 16
		# hex_2 = num % 16
		# Check to see if num is out of the 0-255 range
		if num > 255:
			return "FF"
		elif num < 0:
			return "00"
		else:
			hex_1 = [key for key in hex_digit_dict if hex_digit_dict[key]==num/16]
			hex_2 = [key for key in hex_digit_dict if hex_digit_dict[key]==num%16]
			return hex_1[0] + hex_2[0]
	return_string = get_hex(r) + get_hex(g) + get_hex(b)
	# return return_string
	return return_string

########## call main function
rgb(148,0,211)