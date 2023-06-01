
#text based adventure game
import time # imports library to allow use of time.sleep()
import random


def intro():
	print("#################################################")
	print("##		       Dream Scape					  ##")
	print("#################################################")
	print("-------------------------------------------------")
	print("Would you like to play  [y/n]")

	answer = input(">>")
	if "y" in answer:
		wakeup()
	else:
		print("Please close window")
def wakeup():
	print("You wake up and look around and see you are in middle of a forest somewhere...")
	time.sleep(2)
	print("You head is sore, you lok around and see a path in front of you")
	print("leading deeper into the forest and behind you there is a gate")
	time.sleep(1)
	print("What do you do")
	print("Option 1: go through gate")
	print("Option 2: go deeper into forest")
	answer = input(">>")

	if "1" in answer:
		dreamend()
	elif "2" in answer:
		forest()
	else:
		wakeup()
		


def forest():
	print("You continue to walk further into the forest")
	time.sleep(2)
	print("There are so many trees, it becomes hard to see")
	time.sleep(1)
	print("What do you do...")
	print("Option 1: keep going")
	print("Option 2: turn back")

	answer = input(">>")
	if "1" in answer:
		keepgoing()
	elif "2" in answer:
		turnback()
	else:
		print("Invalid Input try again.")
		forest()

def dreamend():
	print("So you walk towards the gate behind you get close to it")
	time.sleep(2)
	print("You feel a strong jerk in your body")
	time.sleep(2)
	print("You wake up in your bed confused")
	playagain()
	

def keepgoing():
	print("You continue through the forest and find yourself lost and hear a weird noise near to where you are")
	time.sleep(2)
	print("You can't see anything...")
	time.sleep(3)
	print("Suddenly a small, disfigured creature jumps out at you and goes for your throat.")
	print("You are defenceless and accept your fate")
	playagain()

def turnback():
	print("You turn around hoping to find you way back")
	time.sleep(2)
	print("You see a small opening in the trees")
	time.sleep(1)
	print("What do you do...")
	print("Option 1: Walk towards small opening")
	print("Option 2: Try find a different way")

	answer = input(">>")
	if "1" in answer:
		bridgelake()
	elif "2" in answer:
		nootherway()
	else:
		print("Invalid Input try again.")
		turnback()


def nootherway():
	print("You turn around to try and find a different way...")
	time.sleep(1)
	print("You keep going but seem to get more and more lost")
	time.sleep(1)
	print("Eventually you become really weak and unable to see..")
	time.sleep(1)
	print("You are about to pass out you fall to the ground and pass out")
	playagain()

def bridge():

	

	print("You carry on over the bridge as you walk you see what looks like dead bodies in the lake....")
	time.sleep(2)
	print("you hear a feint scream coming from the water")
	time.sleep(4)
	print("You head towards the edge to take a closer look in the lake")
	randomevent = random.randint(0,10)
	if randomevent < 5:
		print("You catch your foot on a brick and fall into the lake")
		time.sleep(2)
		print("You meet you demise and become one of the dead bodies in the lake")
		playagain()
	elif randomevent >= 5:
		print("You take a close look and notices the dead bodies are faceless and shrieking in pain....")
	print("Terrified you carry on towards the path the end of the bridge")
	bridgeend()
	
def bridgelake():
	print("You walk towards the opening and find you are near a lake")
	time.sleep(2)
	print("The air is eerie, and you feel a sense of dread")
	time.sleep(2)
	print("You see a bridge. \n What do you do?")

	print("Option 1: go over bridge")
	print("Option 2: turn around")
	answer = input(">>")
	if "1" in answer:
		bridge()
	elif "2" in answer:
		turnback()
	else:
		print("Invalid Input try again.")
		bridgelake()
		


def bridgeend():

	print("As you near the end of the bridge the trees start to melt around you")
	time.sleep(2)
	print("Horrified you carry on along the path and enter the gate at the end....you sigh in relief")
	time.sleep(2)
	print('You hear a distant whisper "you have beaten the forest of dread"')
	time.sleep(2)
	print("You wake up confused and sweating")
	playagain()



def playagain():
	print("Would you like to play again? Y/N")
	answer = input(">>")
	if "y" in answer:
		wakeup()
	else:
		time.sleep(1000000)

intro()
wakeup()
forest()
dreamend()
turnback()
keepgoing()
bridgelake()
bridge()
nootherway()
bridgeend()
playagain()
