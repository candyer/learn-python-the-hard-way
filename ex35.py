from sys import exit

def palace():
	print "Wow, you are lucky,this is the princess's bed room."
	print "But please be careful, the guards are everywhere."
	print "Speak the devil... watch out!!  do you fight or hide?"
	guards_left = False

	while True:
		next = raw_input("*** ")
		if next == "fight":
			dead("their's a gun pointing at your forhead. you are dead!")
		elif next == "hide" and not guards_left:
			print "you are super lucky today, the guards just walked away."
			guards_left = True
		elif next == "bravo" and guards_left:
			dead("the princess found you, and invite you for a drink")
		else:
			dead("You don't know how to escape, dummy!")

def gold_room():
	 print "This room is full of gold. How much do you take?"

	 next = raw_input("> ")
	 if "0" in next or "1" in next:
	 	how_much = int(next)
	 else:
	 	dead("Man, learn to type a number.")

	 if how_much < 50:
	 	print "Nice, you are not greedy, you win!"
	 	exit(0)
	 else:
	 	dead("You greedy bastard!")

def bear_room():
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	bear_moved = False

	while True:
		next = raw_input("> ")

		if next == "take honey":
			dead("The bear looks at you then slaps your face off.")
		elif next == "taunt bear" and not bear_moved:
			print "The bear has moved from the door. You can go through it now."
			bear_moved = True
		elif next == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		elif next == "open door" and bear_moved:
			gold_room()
		else:
			print "I got no idea what that means."

def Cthulhu_room():
	print "Here you see the great evil Cthulhu."
	print "He, it, whatever stares at you and you go insane."
	print "Do you flee for your life or eat your head?"

	next = raw_input("> ")

	if "flee" in next:
		start()
	elif "head" in next:
		dead("Well that was tasty!")
	else:
		Cthulhu_room()

def dead(why):
	print why,"Good job!"
	exit(0)

def start():
	print "You are in a dark room."
	print "There is a door to your right left or middle."
	print "Which one do you take?"

	next = raw_input(">")

	if next == "left":
		bear_room()
	elif next == "right":
		Cthulhu_room()
	elif next == "middle":
		palace()
	else:
		dead("You stumble around the room until you starve.")

start()
