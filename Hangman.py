print("Hello, which hangman game do you want ")
print ("1.to guess the animal")
print("2.to guess the fruit")
p=int(input("Enter the number :"))
print("\n")
if(p==1):
	import random

	def select_word():
		words = ["Tiger", "dog", "lion", "elephant", "monkey", "pig", "camel","rabbit","mouse","dear","bull","hippo"]
		return random.choice(words)

	def display_word(word, guessed_letters):
		displayed_word = ""
		for letter in word:
		    if letter in guessed_letters:
		        displayed_word += letter
		    else:
		        displayed_word += "_"
		return displayed_word

	def hangman():
		word = select_word()
		guessed_letters = []
		incorrect_guesses = 0
		max_guesses = 6

		print("Welcome to Hangman!")
		print("Guess the animal!")

		while True:
		    print("\nWord:", display_word(word, guessed_letters))
		    guess = input("Guess a letter: ").lower()

		    if len(guess) != 1 or not guess.isalpha():
		        print("Please enter a single alphabetic character.")
		        continue

		    if guess in guessed_letters:
		        print("You've already guessed that letter.")
		        continue

		    guessed_letters.append(guess)

		    if guess in word:
		        print("Correct!")
		    else:
		        incorrect_guesses += 1
		        print("Incorrect guess.")
		        print(f"You have {max_guesses - incorrect_guesses} guesses left.")

		    if incorrect_guesses == max_guesses:
		        print("\nSorry, you've run out of guesses!")
		        print(f"The word was: {word}")
		        break

		    if all(letter in guessed_letters for letter in word):
		        print("\nCongratulations! You've guessed the word!")
		        print(f"The word was: {word}")
		        break

	if _name_ == "_main_":
		hangman()

elif(p==2):
	import random

	def selectword():
		words1 = ["apple", "banana", "orange", "grape", "melon", "strawberry", "peach","mango","lemon","papaya","pineapple"]
		return random.choice(words1)

	def displayword(word1, guessed_letters1):
		displayedword = ""
		for letter in word1:
		    if letter in guessed_letters1:
		        displayedword += letter
		    else:
		        displayedword += "_"
		return displayedword

	def hangman2():
		word1 = selectword()
		guessed_letters1 = []
		incorrect_guesses1 = 0
		max_guesses1 = 6

		print("Welcome to Hangman!")
		print("Guess the fruit!")

		while True:
		    print("\nWord:", displayword(word1, guessed_letters1))
		    guess = input("Guess a letter: ").lower()

		    if len(guess) != 1 or not guess.isalpha():
		        print("Please enter a single alphabetic character.")
		        continue

		    if guess in guessed_letters1:
		        print("You've already guessed that letter.")
		        continue

		    guessed_letters1.append(guess)

		    if guess in word1:
		        print("Correct!")
		    else:
		        incorrect_guesses1 += 1
		        print("Incorrect guess.")
		        print(f"You have {max_guesses1 - incorrect_guesses1} guesses left.")

		    if incorrect_guesses1 == max_guesses1:
		        print("\nSorry, you've run out of guesses!")
		        print(f"The word was: {word1}")
		        break

		    if all(letter in guessed_letters1 for letter in word1):
		        print("\nCongratulations! You've guessed the word!")
		        print(f"The word was: {word1}")
		        break

	if _name_ == "_main_":
		hangman2()
