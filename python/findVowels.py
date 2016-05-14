"""
	Code War Challenge - 7 kyu
	We want to know the index of the vowels in a given word, 
	for example, there are two vowels in the word super 
	(the second and fourth letters).

	So given a string "super", we should return a list of [2, 4].
"""

def vowel_indices(word):
	"""
		This function accepts a string and returns a list
		of the indices of any vowels.
	"""
	# list of vowel locations, will be empty if no vowels are found
	vowels_found = []
	# Constants of the vowels
	VOWELS = ["A", "E", "I", "O", "U", "Y"]

	# start index at the first letter
	index = 1
	for i in word:
		if i.upper() in VOWELS:
			vowels_found.append(index)
		index +=1
	return vowels_found

####### BETA TESTING ########
print vowel_indices("blAhblah")

# ####### Cool solution 
def vowel_indices(word):
    return [i for i,x in enumerate(word,1) if x.lower() in 'aeiouy']