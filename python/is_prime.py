"""
	CodeWars - 6 kyu
"""

def is_prime(num):
	"""
		This function accepts an integer - positive or negative -
		and returns the boolean value of whether its prime of not
	"""
	if abs(num)==1 or num == 0:
		return False
	for x in range(2, abs(num)):
		if num % x == 0:
			return False
	return True
########### Testing
print is_prime(5)

####### Other solutions #########
def is_prime(num):
    return num > 1 and not any(num % n == 0 for n in range(2,num))