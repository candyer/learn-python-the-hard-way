def next_letter(letter):
	return chr(ord(letter) + 1)

def initialize_array(city):
	"""
	create a list of "a" the same length as city
	"""
	list_city = []
	while len(list_city) < len(city):
		list_city.append('a')
	return list_city

def list_to_string(list_city):
	"""
	take a list, make what's inside to a string.
	"""
	return ''.join(list_city) 


def increment_letter(letter_from_list, letter_from_city):
	"""
	take the value from list and string,on the same position,if it's the same, return the same, otherwise increment one
	"""
	if letter_from_list < letter_from_city:
		return next_letter(letter_from_list)
	else:
		return letter_from_city


def increment_list(changing_list, city):
	"""
	compare the initialize_array with list_city, stop running when they are the same.
 	"""
 	n = 0
 	while n < len(changing_list):
 		# print "comparing", changing_list[n], "with", city[n]
 		changing_list[n] = increment_letter(changing_list[n], city[n])
 		n = n + 1
 	return changing_list


def print_board(city):
	changing_list = initialize_array(city)
	print list_to_string(changing_list)
	while list_to_string(changing_list) != city:
		print list_to_string(increment_list(changing_list, city))


print_board("paris")

def tests():
	print initialize_array("paris") == ['a','a','a','a','a']
	print initialize_array("bj") == ['a','a']
	print initialize_array("") == []
	print list_to_string(['p','a','r','i','s']) == "paris"
	print list_to_string([]) == ""
	print increment_letter("a", "p") == "b"
	print increment_letter("b", "p") == "c"
	print increment_letter("p", "p") == "p"
	print increment_list(['i','a','i','i','i'], "paris") == ['j','a','j','i','j']
	print increment_list(['a'], "a") == ['a']
	print increment_list(['a'], "d") == ['b']
