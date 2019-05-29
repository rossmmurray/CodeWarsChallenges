import MyTime
import functools


def sum_dig_pow(a, b):
	eureka_nums = []
	numbers = range(a, b + 1)
	for i in numbers:
		digits = str(i)
		running_total = 0
		for key, digit in enumerate(digits):
			running_total += int(digit) ** (key + 1)
		if running_total == i:
			eureka_nums.append(i)
	return eureka_nums


def sum_dig_pow2(a, b):
	numbers = range(a, b + 1)
	return list(filter(eureka_check, numbers))


def eureka_check(number):
	digits = str(number)
	running_total = 0
	for key, digit in enumerate(digits):
		running_total += int(digit) ** (key + 1)
	return running_total == number


print(sum_dig_pow2(10, 136))
print(sum_dig_pow(10, 136))


MyTime.measure_time([sum_dig_pow2, sum_dig_pow], 10, 1360)

