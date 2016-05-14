"""
	Code Wars - 6 kyu
	sort a string that has a single number in each word
	Each number could be from 1-9. Return an empty string 
	if it is empty
"""

def order(sentence):
  # the return string - global variable
  sorted_sentence = ""
  # if the sentence is not empty then proceed
  if sentence and sentence.strip():
  	# split the string by space & store as a list
  	words_list = sentence.split()
  	# make a new list of the same number of elements
  	copy_list = list(words_list)
  	# for each word in the words_list
  	for word in words_list:
  		number = 0
  		# go through each letter in word to find a number
  		for letter in word:
  			if letter.isdigit():
  				number = int(letter)
  		copy_list[number - 1] = word
  	#write the sentence
  	for word in copy_list:
  		sorted_sentence += word
  		sorted_sentence += " "
  	# take away the last space
  	sorted_sentence = sorted_sentence.rstrip()

  # assumes that the string is empty here
  else:
  	sorted_sentence = sentence

  # code here
  return sorted_sentence


  ######## beta testing ######
print order("is2 Thi1s T4est 3a")

##### Cool solution I found #######
def order(sentence):
    return " ".join(sorted(sentence.split(), key=lambda x: int(filter(str.isdigit, x))))