"""
	Code Wars - 7 kyu
	takes a string as input and return an object containing the properties vowels and consonants. 
	The vowels property must contain the total count of vowels {a,e,i,o,u}, and the total count 
	of consonants {a,..,z} - {a,e,i,o,u}. Handle invalid input and don't forget to return valid ones.
"""
import pprint

def get_count(*words):
	#initalize return dict
    output_dict = {"vowels": 0, "consonants": 0}
    # constants, of the vowels
    VOWELS = ["A", "E", "I", "O", "U", "Y"]
    if not words:
    	pass
    else:
    	# Count vowels and consonants:
    	for i in words[0]:
    		if i.upper() in VOWELS:
    			output_dict["vowels"]+=1
    		elif i == " ":
    			pass
    		else:
    			output_dict["consonants"]+=1
    return output_dict


##### TESTING
pprint.pprint(get_count("aB"))