import functools


def pow_add(power, x, y):
	result = int(x) ** power + int(y)
	print(f'power: {power}, x: {x}, y: {y}, result: {result}')
	return result


def narcissistic(value):
	str_val = str(value)
	digit_count = len(str_val)
	specific_pow_add = functools.partial(pow_add, digit_count)
	# specific_pow_add(4, 8)
	# return specific_pow_add(1, 2)
	return functools.reduce(specific_pow_add, str_val)

	# return str_val[4]


print(narcissistic(153))
