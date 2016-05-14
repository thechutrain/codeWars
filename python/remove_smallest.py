def remove_smallest(numbers):
    # raise NotImplementedError("TODO: remove_smallest")
    new_list = []
    try:
	    lowest_num = numbers[0]
	    lowest_num_index = 0
	    index = 0
	    # find the lowest number by looping through every element in list
	    for i in numbers:
	    	if lowest_num > i:
	    		lowest_num = i
	    		lowest_num_index = index
	    	index +=1
	    new_list = list(numbers)
	    del new_list[lowest_num_index]
    except IndexError as e:
		print "Error"
    return new_list


test_list = [2,3,4,5, 1]
test = []
remove_smallest(test)


######### Short solution ########
def remove_smallest(numbers):
    if numbers:
        numbers.remove(min(numbers))
    return numbers