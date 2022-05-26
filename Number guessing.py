import random

game_is_on = True
the_number = random.randint(1, 100)
print("Guess a number between 1 and 100 that computer chose randomly")
difficulty = input("Choose your difficulty ''hard'' or ''easy''\n").lower()

def hard():
	guesses = 5
	# print(f"pss the number is {the_number}")
	while guesses > 0:
		print(f"You have {guesses} guesses remaining")
		my_guess = int(input("Make a guess"))
		if my_guess > the_number:
			guesses -= 1
			if guesses > 0:
				print("Too high")
				print("Guess Again")
			if guesses == 0:
				print("You ran out of guesses , you lose")
		elif my_guess < the_number:
			guesses -= 1
			if guesses > 0:
				print("Too low")
				print("Guess Again ")
			if guesses == 0:
				print("You ran out of guesses , you lose")
		if my_guess == the_number:
			print("Congratulations you guesses the correct number !")
			guesses = 0

def easy():
	guesses = 10
	# print(f"pss the number is {the_number}")
	while guesses > 0:
		print(f"You have {guesses} guesses remaining")
		my_guess = int(input("Make a guess"))
		if my_guess > the_number:
			guesses -= 1
			if guesses > 0:
				print("Too high")
				print("Guess Again")
			if guesses == 0:
				print("You ran out of guesses , you lose")
		elif my_guess < the_number:
			guesses -= 1
			if guesses > 0:
				print("Too low")
				print("Guess Again ")
			if guesses == 0:
				print("You ran out of guesses , you lose")
		if my_guess == the_number:
			print("Congratulations you guesses the correct number !")
			guesses = 0


if difficulty == "hard":
	hard()
else:
	easy()