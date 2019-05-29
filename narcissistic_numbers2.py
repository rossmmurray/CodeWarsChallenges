import timeit


# my one
def narcissistic(value):
	str_val = str(value)
	digit_count = len(str_val)
	result = sum(map(lambda x: int(x) ** digit_count, str_val))
	return result == value


# best one apparently
def narcissistic2(value):
	return value == sum(int(x) ** len(str(value)) for x in str(value))


def wrapper(func, *args, **kwargs):
	def wrapped():
		return func(*args, **kwargs)
	return wrapped


no_args = wrapper(narcissistic, 153)

print(timeit.timeit(no_args))
