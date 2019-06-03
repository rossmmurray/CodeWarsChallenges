from typing import List, Dict


def namelist(names):
	if len(names) == 0: return ''
	if len(names) == 1: return names[0]['name']
	name_string = ''
	for name in names[0: -2]:
		name_string = name_string + name['name'] + ', '
	name_string = name_string + names[-2]['name'] + ' & ' + names[-1]['name']
	return name_string


def namelist2(names):
	names_list = [name_dict['name'] for name_dict in names]
	if len(names) == 0:
		return ''
	if len(names) == 1:
		return names_list[0]
	name_string = ', '.join(names_list[:-1]) + ' & ' + names_list[-1]
	return name_string


print(namelist2([{'name': 'Homer'}, {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]))
print(namelist2([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]))
print(namelist2([{'name': 'Bart'}, {'name': 'Lisa'}]))
print(namelist2([{'name': 'Bart'}]))
