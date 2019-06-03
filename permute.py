from typing import List, AnyStr


def permutations(string):
	string = list(string)
	xperm(string)


def xperm(string):

	if len(string) == 1:
		return string
	for i in range(len(string)):
		new_string = string.copy()

		# fix first element
		new_string[0], new_string[i] = new_string[i], new_string[0]

		temp = [new_string[0]].copy() + xperm(new_string[1:].copy())
		print(temp)




print(permutations('abcdefghi'))