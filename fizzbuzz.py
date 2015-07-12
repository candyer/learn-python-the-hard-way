numbers = range(100)

for number in numbers:

	if number % 3 == 0 and number % 5 == 0:
		print "fizzbuzz"
		
	elif number % 3 == 0:
		print "fizz"

	elif number % 5 == 0:
		print "buzz"

	else:
		print " %d " % number
