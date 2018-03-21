from random import randint 

#computer chooses a number
numb_comp = randint(1,10)
#ask user for guess
numb_guess = None

while numb_guess != numb_comp:
	numb_guess = int(input("Guess a number between 1 and 10: "))
	if (numb_guess > 0) and (numb_guess < 11):
		if numb_guess < numb_comp:
			print("TOO LOW SUCKER")
		elif numb_guess > numb_comp:
			print("TOO MUTHAFUCKIN HIGH")
		else:
			print("YOU FUCKER!!! YOU WON!!!")
			again = input("Play again? y/n ")
			if again == "y":
				numb_guess = None
			else: 
				print("GOODBYE FUCKER")
	else:
		print("THAT AIN'T NO MUTHAFUCKIN VALID INPUT.")