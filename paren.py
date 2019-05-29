def valid_parentheses(string):
	running_sum = 0
	paren_map = {'(': 1, ')': -1}
	for char in string:
		running_sum += paren_map.get(char, 0)
		if running_sum < 0:
			return False
	return True if running_sum == 0 else False


print(valid_parentheses("hi())("))
