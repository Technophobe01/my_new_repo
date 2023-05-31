import random
import string


class Hangman:
    def __init__(self):
        self.word_list = ["python", "java", "swift", "javascript"]
        self.wins = 0
        self.losses = 0

    def start(self):
        print('H A N G M A N')
        while True:
            choice = input(
                'Type "play" to play the game, "results" to show '
                'the scoreboard, and "exit" to quit: ')

            if choice == "play":
                self.play()
            elif choice == "results":
                self.show_results()
            elif choice == "exit":
                self.exit_game()
            else:
                print("Invalid choice. Please try again.\n")

    def play(self):
        # Choose a word at random from the list
        word = random.choice(self.word_list)

        # Print the welcome message
        attempts_left = 8

        # Create a set of letters in the word
        word_letters = set(word)

        # Create a set of guessed letters
        guessed_letters = set()

        # Initialize flag variable to keep track of
        # whether the game is over or not
        game_over = False

        # Loop until the game is over
        while not game_over:
            # Print the current progress
            print("" + "".join([letter
                                if letter in guessed_letters
                                else "-" for letter in word]))

            # If no attempts are left, end the game
            if attempts_left == 0:
                print("You lost!")
                self.losses += 1
                game_over = True
                break

            # Check if the player has guessed all the letters
            if word_letters <= guessed_letters:
                print(f"You guessed the word {word}!")
                print("You survived!")
                self.wins += 1
                game_over = True
                break

            # Ask the player to guess a letter
            guess = input("Input a letter: ")

            if len(guess) != 1:
                print("Please, input a single letter\n")
            elif guess not in string.ascii_lowercase:
                print(
                    "Please, enter a lowercase letter "
                    "from the English alphabet\n")
            elif guess in guessed_letters:
                print("You've already guessed this letter.\n")
            # Check if the letter is in the word
            elif guess in word:
                guessed_letters.add(guess)
                print("")
            # If the letter is not in the word
            else:
                guessed_letters.add(guess)
                print("That letter doesn't appear in the word.\n")
                attempts_left -= 1

        # Print the final message and show the menu again
        print("Thanks for playing!\n")

    def show_results(self):
        print(f"You won: {self.wins} times")
        print(f"You lost: {self.losses} times\n")

    @staticmethod
    def exit_game():
        print("Goodbye!")
        exit()


hangman = Hangman()
hangman.start()
