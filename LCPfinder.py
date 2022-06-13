#!/usr/bin/env python3

def find_the_longest_common_prefix_amongst_all(given_string_array):
	
	# given_string_array is the given array of strings we need to find LCP amongst 
	# If the strings do not have any common prefix, return the empty string as the base case
	
	if not given_string_array:
		
		return ""
	
	# if there is LCP in the given array of strings 
	# use min(array of strings, key = len) here to find the smallest string based on length 
	# the smallest-lengthed-string must contain the LCP if there is LCP 
	# now we have LCP_amongst_all as a new list of strings with the minimum lengths out of the given_string_array 
	
	LCP_amongst_all = min(given_string_array, key = len)
	
	
	#generate counter and current character pairs for each CP character in iterable LCP_amongst_all list of strings

	for counter, current_character in enumerate(LCP_amongst_all):
		
		# traverse the rest characters in the original given array of strings
		# recursively append the CP characters while traversalling
		
		for the_rest_characters in given_string_array:
			
			# if no other characters as the same as current_character 
			# then we know from 0 to counter index position in LCP_amongst_all is the ultimate LCP we are looking for 
			# so we return LCP_amongst_all[:counter] = LCP_amongst_all[0:counter]
			# colon here indicates returning character elements from index 0 to index counter as our LCP range. 
			
			if the_rest_characters[counter] != current_character:
				
				return LCP_amongst_all[:counter]
			
	return LCP_amongst_all 

#driver

# test if the strings do not have any common prefix, return the empty string 

print(find_the_longest_common_prefix_amongst_all(["apple", "app", "aple", "appl"]))

#empty_string = ""

#print(find_the_longest_common_prefix_amongst_all(empty_string))	
		
