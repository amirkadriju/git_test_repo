import getpass

class Hangman:
    # initialize the game
    def __init__(self) -> None:
        self.winningWord = getpass.getpass('Write in the word to guess: ').lower()
        self.guesses = []
        self.guessesLeft = 8
        self.won = False

        # get ascii Art as list
        with open('./git_test_repo/hangmanASCII.txt', 'r') as file:
            content = file.read()
            self.hangmanList = content.split(',')

    def displayStatusandWord(self):
        print(self.hangmanList[-self.guessesLeft])
        print(' '.join([letter if letter in self.guesses else '_' for letter in self.winningWord]))

    def checkGuess(self, guess):
        guess = guess.lower()
        if guess in self.guesses:
            print("You already guessed that letter.")
        elif guess in self.winningWord:
            print(f"Good guess! '{guess}' is in the word.")
            self.guesses.append(guess)
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            self.guesses.append(guess)
            self.guessesLeft -= 1

    def checkWIN(self):
        if all(letter in self.guesses for letter in self.winningWord):
            self.won = True
            return True
        return False

    def play(self):
        print("Welcome to Hangman!")
        while self.guessesLeft > 1 and not self.won:
            self.displayStatusandWord()
            print(f"Attempts left: {self.guessesLeft - 1}")
            print(self.guesses)
            
            guess = input("Guess a letter: ").strip()
            if len(guess) != 1 or not guess.isalpha():
                print("Please guess a single letter.")
                continue

            self.checkGuess(guess)
            if self.checkWIN():
                print("\nCongratulations! You've guessed the word:", self.winningWord)
                break
        else:
            if not self.won:
                print("\nGame over! The word was:", self.winningWord)
                self.displayStatusandWord()

if __name__ == "__main__":
    game = Hangman()
    game.play()
