# todo: turn into a class
import timeit


def wrapper(func, *args, **kwargs):
	def wrapped():
		return func(*args, **kwargs)
	return wrapped


def measure_time(func_list, *args):
	for func in func_list:
		no_arg_func = wrapper(func, *args)
		time_taken = timeit.timeit(no_arg_func, number=1000)
		rounded_time_taken = round(time_taken * 10, 3)
		print(f'{func.__name__}: \t {rounded_time_taken}')
