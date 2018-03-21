import random
playerscore = 0
compscore = 0

print("Hello puny human, let's play Rock, Paper, Scissors. Best two out of three wins.")


while (playerscore <= 2) and (compscore <= 2):
	player = input("Human challenger, make your move: ").lower()
	rand_num = random.randint(0,2)

	if rand_num == 0:
		computer = "rock"
	elif rand_num == 1:
		computer = "paper"
	else:
		computer = "scissors"


	if player == computer:
		print("It's a tie!")
		playerscore = playerscore + 1
		compscore = compscore + 1
	elif player == "rock":
		if computer == "scissors":
			print("Human, you win!")
			playerscore = playerscore + 1
		elif computer == "paper":
			print("The robots have won")
			compscore = compscore + 1
	elif player == "paper":
		if computer == "scissors":
			print("Robots win!")
			compscore = compscore + 1
		elif computer == "rock":
			print("Humans are victorious... this time.")
			playerscore = playerscore + 1
	elif player == "scissors":
		if computer == "rock":
			print("Computer wins. Sorry.")
			compscore = compscore + 1
		elif computer == "paper":
			print("Humans are the winners")
			playerscore = playerscore + 1
	else:
		print("Something went wrong. Uh oh!")

	print(f"\U0001f468  score: {playerscore}, \U0001f916  score: {compscore}")

if playerscore > 2:
	print("The HUMAN has WON!")
else:
	print("Robots will always win. GAME OVER.")
	