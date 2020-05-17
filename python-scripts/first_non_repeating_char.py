def first_non_repeating_char(string):
	rejection_set = set()
	candidate_set = set()

	for char in string:
		if char in candidate_set:
			candidate_set.remove(char)
			rejection_set.add(char)
		elif char not in rejection_set:
			candidate_set.add(char)

	for char_idx in range(len(string)):
		if string[char_idx] in candidate_set:
			return char_idx
	return -1

if __name__ == '__main__':
	test_cases = {
		'aaabcdef' : 3,
		'aaaaaa' : -1,
		'abcdef' : 0,
		'aaabbcceed' : 9
	}
	for test_case, answer in test_cases.items():
		print("{} : {}".format(test_case, first_non_repeating_char(test_case)))
		assert(first_non_repeating_char(test_case) == answer), "Assertion failed for test case : {}".format(test_case)

	print("Success")