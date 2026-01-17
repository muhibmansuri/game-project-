import random
import string

class Hangman:
    def __init__(self):
        self.words = [
            "PYTHON", "DEVELOPER", "ALGORITHM", "FUNCTION", "VARIABLE", 
            "RECURSION", "ITERATOR", "GENERATOR", "DECORATOR", "COMPREHENSION",
            "INTERFACE", "FRAMEWORK", "DATABASE", "DEBUGGING", "SYNTAX"
        ]
        self.word = random.choice(self.words)
        self.word_letters = set(self.word)  # Letters in the word
        self.alphabet = set(string.ascii_uppercase)
        self.used_letters = set()  # What the user has guessed
        self.lives = 6
        self.current_state = 'playing' # win, lose, playing

    def guess(self, letter):
        letter = letter.upper()
        if letter in self.used_letters:
            return "You have already used that character."
        
        if letter in self.alphabet:
            self.used_letters.add(letter)
            if letter in self.word_letters:
                self.word_letters.remove(letter)
            else:
                self.lives -= 1
        
        self.update_state()
        return None

    def update_state(self):
        if len(self.word_letters) == 0:
            self.current_state = 'win'
        elif self.lives == 0:
            self.current_state = 'lose'

    def get_info(self):
        """Returns the current game state for the UI."""
        # Show guessed letters, hide others with dashes
        current_word_list = [letter if letter in self.used_letters else '-' for letter in self.word]
        return {
            'word_display': ' '.join(current_word_list),
            'lives': self.lives,
            'used_letters': sorted(list(self.used_letters)),
            'status': self.current_state,
            'secret_word': self.word if self.current_state != 'playing' else None
        }

if __name__ == '__main__':
    game = Hangman()
    print(game.word)
    while game.current_state == 'playing':
        print(game.get_info()['word_display'])
        guess = input("Guess a letter: ")
        game.guess(guess)
    print(f"Game Over: {game.current_state}")
