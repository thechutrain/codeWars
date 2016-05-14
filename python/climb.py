"""
	For every positive integer N, there exists a unique sequence starting with 1
	and ending with N and such that every number in the sequence is either the double
	 of the preceeding number or the double plus 1.

	For example, given N = 13, the sequence is [1, 3, 6, 13], because . . . :
"""

#### MY solution - just okay, could be a lot better

def climb(n):
	"""
		this function will return a list containing
		the factors that multiply up 
	"""
	return_list = [n]
	keep_looping = True
	while keep_looping:
		# if the last element in the list is 1 exit
		if return_list[-1] == 1:
			keep_looping = False
		#elif its even!
		elif return_list[-1] % 2 == 0:
			next_number = return_list[-1] / 2
			return_list.append(next_number)
		# else its odd
		else:
			next_number = (return_list[-1] - 1) / 2
			return_list.append(next_number)
	reversed_list = return_list[::-1]
	return reversed_list
	# return return_list

#Better solution
def climb(n):
    return [1] if n == 1 else climb(int(n/2)) + [n]

def my_climb(n):
	if n == 1:
		return [1]
	else:
		return climb(int(n/2)) + [n]

#### TESTING 
# print climb(10)
print my_climb(5)


