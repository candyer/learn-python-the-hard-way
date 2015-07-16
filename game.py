def game_while(to_guess):
	print "guess a number:"
	number = int(raw_input("> "))
	while number != to_guess:
		if number < to_guess:
			print "too small"
		else:
			print "too big"
		print "guess again:"
		number = int(raw_input("> "))
	print "you win !"

def game_recursive(to_guess):
	print "guess a number:"
	number = int(raw_input("> "))
	if number < to_guess:
		print "too small"
		game_recursive(to_guess)
	elif number > to_guess:
		print "too big"
		game_recursive(to_guess)
	else:
		print "you win !"

def game_break(to_guess):
	while True:
		print "guess a number:"
		number = int(raw_input("> "))
		if number < to_guess:
			print "too small"
		elif number > to_guess:
			print "too big"
		else:
			print "you win !"
			break

def game_break2(to_guess):
	while True:
		print "guess a number:"
		number = int(raw_input("> "))
		if number == to_guess:
			print "you win !"
			break
		elif number > to_guess:
			print "too big"
		else:
			print "too small"


game_while(90)
game_recursive(45)
game_break(-1)