def unite_unique(*args):
	# list that Ill return
	answer_list = []
	if args:
		# assume the tuple is not empty, loop through
		for list_item in args:
			for item in list_item:
				if item not in answer_list:
					answer_list.append(item)
	else:
		print "empty"
	return answer_list
    # list_return = 
######### TEST #########
print unite_unique(["1", "2"], ["2"], ["2", "3"])


############ OTher solution
def unite_unique(*args):
    result = []
    for a in args:
        for b in a:
            if b not in result:
                result.append(b)
    return result