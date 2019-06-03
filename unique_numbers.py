from typing import List
import MyTime


def find_uniq(arr: List):
	if arr[0] == arr[1]:
		dup = arr[0]
	else:
		dup = arr[0] if arr[0] == arr[2] else arr[1]
	return next(filter(lambda x: x != dup, arr))


def find_uniq2(arr):
	a, b = set(arr)
	return a if arr.count(a) == 1 else b


test_array = [44 for i in range(0, 10000)]
test_array[777] = 2
print(find_uniq2([0, 0, 0.55, 0, 0]))
print(find_uniq2(test_array))
MyTime.measure_time([find_uniq, find_uniq2], test_array)
