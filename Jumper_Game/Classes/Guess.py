from io import StringIO
from Puzzle import Puzzle


class Guess:

    """This class is in charge of the player´s guessing letter part

    attributes:

    methods:

    """

    def __init__(self):
        secret_word = Puzzle.get_random_word(Puzzle())
        self.letters_word = self.Puzzle.letters_word
        self.letters_hidden = []

    def guess_letter(self):
        ask = input('Guess a letter [a-z]: ')
        ask = ask.strip().lower

        valid_word = self.Puzzle.check_letters(ask)
        if valid_word:
            self.do_inputs = ask[0]
        else:
            print("That's not a valid character...")
        pass
    def list_dashes(self):
        for i in range(len(self.letters_word)):
            self.letters_hidden.append('_')

    def check_letters(self, character) -> bool:
        stringg = StringIO.ascii_lowercase
        listt = list(stringg)
        if character in listt:
            return True
        else:
            return False
    def check_guessed(self):
        # Chek if the letter choosed by the user is in the secret word, and remplace the dashes if there is the letter. 
         if self.do_inputs in self.letters_word:
             for i in range (len(self.letters_word)):
                 if self.do_inputs == self.letters_word[i]:
                     self.letters_hidden[i] = self.do_inputs
                     pass


    def reveal_word():
        pass
