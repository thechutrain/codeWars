"""
	Codewars - 7 kyu
"""
# My solution

def rake_garden(garden):
	"""
		This string accepts a string representing the garden
		and filters anything that is not a rock or gravel, by
		replacing all non-garden objects with gravel.
	"""
	cleaned_garden = ""
	# convert the garden into a list:
	garden_list = garden.split(" ")
	for index, item in enumerate(garden_list):
		if not (item == "gravel" or item == "rock"):
			garden_list[index] = "gravel"
	for x in garden_list:
		cleaned_garden = cleaned_garden + x + " "
	cleaned_garden = cleaned_garden.rstrip()
	return cleaned_garden


###### OTHER BETTER SOLUTIONS #########
VALID = {'gravel', 'rock'}

def rake_garden(garden):
    return ' '.join(a if a in VALID else 'gravel' for a in garden.split())


import re
def rake_garden(garden):
    return re.sub(r'(?<!\S)(?!gravel|rock)\S+', 'gravel', garden)

###### testing
rake_garden('gravel slug gravel rock gravel gravel gravel gravel gravel gravel gravel')