
# basic fizbuz solution
def fizbuz():
	for num in range(1, 101):
		if num % 15 == 0:
			print 'fizbuz'
		elif num % 5 == 0:
			print 'buz'
		elif num % 3 == 0:
			print 'fiz'
		else:
			print num
# fizbuz()


# fizbuz solution without division, version 1
def fizbuz1():
	mod3 = mod5 = mod15 = 0
	for num in range(1, 101):
		mod3 += 1
		mod5 += 1
		mod15 += 1
		if mod15 == 15:
			print 'fizbuz'
			mod3 = mod5 = mod15 = 0
		elif mod5 == 5:
			print 'buz'
			mod5 = 0
		elif mod3 == 3:
			print 'fiz'
			mod3 = 0
		else:
			print num
# fizbuz1()


# fizbuz solution without division, version 2
def fizbuz2():
	mod3, mod5 = 3, 5
	for num in range(1, 101):
		if num == mod3 == mod5:
			print 'fizbuz'
			mod3 += 3 
			mod5 += 5
		elif num == mod5:
			print 'buz'
			mod5 += 5
		elif num == mod3:
			print 'fiz'
			mod3 += 3
		else:
			print num
# fizbuz2()


# fizbuz solution without division, version 3
def fizbuz3():
	array = [1, 2, 'fiz', 4, 'buz', 'fiz', 7, 8, 'fiz', 'buz', 11, 'fiz', 13, 14, 'fizbuz']
	pos = count = 0
	for num in range(100):
		tmp = array[num % 15]
		if type(tmp) == int:
			print tmp + 15 * count
		else:
			if tmp == 'fizbuz':
				count += 1
			printtmp


# fizbuz3()
