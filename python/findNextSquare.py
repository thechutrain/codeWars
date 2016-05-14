"""
	Code Wars - 7 Kyu

"""
import math
# sqrt function returns a float

def findNextSquare(number):
	"""
		This function accepts a perfect square, and finds 
		the next perfect square - i.e. given 9, it gives 16.

		If the argument is not a perfect square then it returns
		- 1
	"""
	# assume the author gives a non-perfect square
	return_int = -1
	# converts the float of sqrt to a the int below it
	# print int(math.sqrt(number))
	bottom_int = int(math.sqrt(number))
	top_int = bottom_int + 1

	# check to see if argument was a perfect square
	if number == float(bottom_int**2):
		return_int = top_int ** 2
	else:
		# not a perfect square, do not change return_int
		pass
	return return_int

######## testing ###########
print findNextSquare(25)

######## ANOTHER SOLUTION ##########
def find_next_square(sq):
    root = sq ** 0.5
    if root.is_integer():
        return (root + 1)**2
    return -1

