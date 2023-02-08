import random
import math
"""
number=random.randrange(1,70)
					while number in g[]:
						number=random.randrange(1,70)
					g[i]=number
number=random.randrange(1,27)
					while number in g[]:
						number=random.randrange(1,27)
					g[i]=number
"""

while (1):
	p=[0]*6
	g=[0]*6
	w=[0]*6
	print("Welcome to the powerball! Choose six numbers to see if you win!")
	for i in range(0,6):
		if i<5:
			while (1):
				g[i]=random.randrange(1,70)
				#print("GAME NUMBER ", g[i])
				p[i] = input("White ball #" + str(i+1)+ ": ")
				while (p[i].isdigit()==False):
					p[i]=input("White ball #"+ str(i+1)+ " Enter a NUMBER with no letters! : ")
				p[i]=math.floor(float(p[i]))
				if p[i]>69 or p[i]<1:
					print("Pick a number between 1 and 69.")
				else:
					
					break
		else:
			while (1):
				g[i]=random.randrange(1,27)
				#print("GAME NUMBER ", g[i])
				p[i] = input("Powerball: ")
				while (p[i].isdigit()==False):
					p[i]=input("Powerball! Enter a NUMBER with no letters!")
				p[i]=math.floor(float(p[i]))
				if p[i]>26 or p[i]<1:
					print("Pick a number between 1 and 26.")
				else:
					
					break
	for i in range(0,6):
		if i<5:
			print("#", i+1, "YOU PICKED: ", p[i], "YOU GOT: ", g[i])
		else:
			print("POWERBALL", i+1, "YOU PICKED: ", p[i], "YOU GOT: ", g[i])
		if p[i]==g[i]:
			w[i]=1
	if sum(w)==1 and w[5]==1:
		print("Your powerball matched! You win 4 DOLLARS!")
	elif sum(w)==1:
		print("You matched one white ball. No reward :(")
	elif sum(w)==2 and w[5]==1:
		print("You matched a white ball and a powerball! You win 4 DOLLARS!")
	elif sum(w)==2:
		print("You matched two white balls! No reward :(")
	elif sum(w)==3 and w[5]==1:
		print("You matched two white balls and a powerball! You win 7 DOLLARS!")
	elif sum(w)==3:
		print("You matched three white balls! You win 7 DOLLARS!")
	elif sum(w)==4 and w[5]==1:
		print("You matched three white balls and a powerball! You win 100 DOLLARS!")
	elif sum(w)==4:
		print("You matched four white balls! You win 100 DOLLARS!")
	elif sum(w)==5 and w[5]==1:
		print("You matched four white balls and a powerball! You win 50,000 DOLLARS!")
	elif sum(w)==5:
		print("You matched five white balls! You win 1,000,000 DOLLARS!")
	elif sum(w)==6:
		print("You matched all your balls! JACKPOT!!!")
	
	print("\n")
	
