from random import *
import os
from unicurses import *

playerName = ""
cardName = ""
cardName2 = ""
bootAmount = 10
bet = 0
crntBet1 = 10
suits = ["Hearts","Spades","Diamonds","Clubs"]
name = ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
player = {}
cpu = {}

def splash():
	os.system('cls')
	i=0
	j=0
	print("="*114)
	while i<10:
		print("||"+"\t"*14+"||")
		i=i+1
	print("||"+"\t"*6+"+-----------------------+"+"\t"*5+"||")
	print("||"+"\t"*6+"| "+"Welcome to TEEN PATTI"+" |"+"\t"*5+"||")
	print("||"+"\t"*6+"+-----------------------+"+"\t"*5+"||")
	print("||"+"\t"*6+"Press 1 to continue!!"+"\t"*6+"||")
	while j<10:
		print("||"+"\t"*14+"||")
		j=j+1
	print("="*114)
	c = input()
	if c == '1':
		initialize()
		
def header():
	print("="*114)
	print("\t"*5+"TEEN PATTI")
	print("="*114)

def initialize():
	global playerName
	global bet
	
	os.system('cls')
	header()
	playerName = input("Enter you Name:\t")
	print("WELCOME MR "+playerName)	
	c = input("Press d to distribute cards\n")
	if c == 'd':
		print("Collecting Boot Amount of Rs 10")
		print("BET = "+str(bet)+" rs")
		dist()
		gamePlay()

def gamePlay():
	choice = 0
	os.system('cls')
	header()
	while choice!=4:
		try:
			print("\n\n1. BLIND\n2. SEE\n3. INCREASE BET\n4. SHOW\n")
			choice = int(input())
			if choice == 1:
				blind()
			elif choice == 2:
				see()
			elif choice == 3:
				increaseBet()
			elif choice == 4:
				show()
			else:
				print("Command not found")
		except:
			print("Command not found")
			
def blind():
	global bet
	global bootAmount
	global crntBet1
	
	bet = bet+bootAmount+crntBet1
	print("BET = "+str(bet)+" rs")
	
def see():
	global player
	print("PLAYER CARDS:\n")
	print(player["card1"]+"\n"+player["card2"]+"\n"+player["card3"])
	
def show():
	global player
	global cpu
	
	print("PLAYER CARDS:\n")
	print(player["card1"]+"\n"+player["card2"]+"\n"+player["card3"])
	print("\nCPU CARDS:\n")
	print(cpu["card1"]+"\n"+cpu["card2"]+"\n"+cpu["card3"])
	
	if player_precedence() > cpu_precedence():
		print("\n\nPlayer WINS")
		print(cardName)
	elif player_precedence() == cpu_precedence():
		if checkNextCard() == True:
			print("\n\nPlayer WINS\nHIGH CARD")
		else:
			print("\n\nCPU WINS\nHIGH CARD")
	else:
		print("\n\nCPU WINS")
		print(cardName2)
	
def dist():
	global suits
	global name
	global player
	global cpu
	
	player["suit1"] = randint(0,3)
	player["n1"] = randint(0,12)
	player["suit2"] = randint(0,3)
	player["n2"] = randint(0,12)
	player["suit3"] = randint(0,3)
	player["n3"] = randint(0,12)
	player["card1"] = name[player["n1"]]+" of "+suits[player["suit1"]]
	player["card2"] = name[player["n2"]]+" of "+suits[player["suit2"]]
	player["card3"] = name[player["n3"]]+" of "+suits[player["suit3"]]
	
	cpu["suit1"] = randint(0,3)
	cpu["n1"] = randint(0,12)
	cpu["suit2"] = randint(0,3)
	cpu["n2"] = randint(0,12)
	cpu["suit3"] = randint(0,3)
	cpu["n3"] = randint(0,12)
	cpu["card1"] = name[cpu["n1"]]+" of "+suits[cpu["suit1"]]
	cpu["card2"] = name[cpu["n2"]]+" of "+suits[cpu["suit2"]]
	cpu["card3"] = name[cpu["n3"]]+" of "+suits[cpu["suit3"]]
	
def isSequencePlayer():
	if player["n1"] == player["n2"]+1 and player["n1"] == player["n3"]+2:
		return True
	elif player["n1"] == player["n2"]+2 and player["n1"] == player["n3"]+1:
		return True
	elif player["n1"] == player["n2"]+1 and player["n1"] == player["n3"]-1:
		return True
	elif player["n1"] == player["n2"]-1 and player["n1"] == player["n3"]+1:
		return True
	elif player["n1"] == player["n2"]-1 and player["n1"] == player["n3"]-2:
		return True
	elif player["n1"] == player["n2"]-2 and player["n1"] == player["n3"]-1:
		return True
	else:
		return False
		
def isSequenceCPU():
	if cpu["n1"] == cpu["n2"]+1 and cpu["n1"] == cpu["n3"]+2:
		return True
	elif cpu["n1"] == cpu["n2"]+2 and cpu["n1"] == cpu["n3"]+1:
		return True
	elif cpu["n1"] == cpu["n2"]+1 and cpu["n1"] == cpu["n3"]-1:
		return True
	elif cpu["n1"] == cpu["n2"]-1 and cpu["n1"] == cpu["n3"]+1:
		return True
	elif cpu["n1"] == cpu["n2"]-1 and cpu["n1"] == cpu["n3"]-2:
		return True
	elif cpu["n1"] == cpu["n2"]-2 and cpu["n1"] == cpu["n3"]-1:
		return True
	else:
		return False
		
	
def player_precedence():
	global player
	global cardName
	
	if player["n1"] == player["n2"] and player["n1"] == player["n3"]:
		cardName = "TRIPLET"
		return 18
	elif isSequencePlayer() == True:
		cardName = "SEQUENCE"
		return 17
	elif player["suit1"] == player["suit2"] and player["suit1"] == player["suit3"]:
		cardName = "COLOR"
		return 15
	elif player["n1"] == player["n2"] or player["n1"] == player["n3"] or player["n2"] == player["n3"]:
		cardName = "DOUBLET"
		return 14
	else:
		cardName = "HIGH CARD"
		if player["n1"] > player["n2"] and player["n1"] > player["n3"]:
			return player["n1"]
		elif player["n2"] > player["n1"] and player["n2"] > player["n3"]:
			return player["n2"]
		else:
			return player["n3"]
		
def cpu_precedence():
	global cpu
	global cardName2
	
	if cpu["n1"] == cpu["n2"] and cpu["n1"] == cpu["n3"]:
		cardName2 = "TRIPLET"
		return 18
	elif isSequenceCPU() == True:
		cardName2 = "Sequence"
		return 17
	elif cpu["suit1"] == cpu["suit2"] and cpu["suit1"] == cpu["suit3"]:
		cardName2 = "COLOR"
		return 15
	elif cpu["n1"] == cpu["n2"] or cpu["n1"] == cpu["n3"] or cpu["n2"] == cpu["n3"]:
		cardName2 = "DOUBLET"
		return 14
	else:
		cardName2 = "HIGH CARD"
		if cpu["n1"] > cpu["n2"] and cpu["n1"] > cpu["n3"]:
			return cpu["n1"]
		elif cpu["n2"] > cpu["n1"] and cpu["n2"] > cpu["n3"]:
			return cpu["n2"]
		else:
			return cpu["n3"]
			
def checkNextCard():
	global player
	global cpu
	
	if player["n1"] > cpu["n1"] and player["n1"] > cpu["n2"] and player["n1"] > cpu["n3"]:
		return True
	elif player["n2"] > cpu["n1"] and player["n2"] > cpu["n2"] and player["n2"] > cpu["n3"]:
		return True
	elif player["n3"] > cpu["n1"] and player["n3"] > cpu["n2"] and player["n3"] > cpu["n3"]:
		return True
	else:
		return False

splash()	
