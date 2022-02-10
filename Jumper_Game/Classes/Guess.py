from Classes.Puzzle import Puzzle


class Guess:

    """This class is in charge of the player´s guessing letter part

    attributes:

    methods:

    """

    def __init__(self):

        #choose a random word
        self.secret_word = Puzzle.get_random_word(Puzzle())
        self.tries = 6
        self.guessed = False
        self.guessed_letters = []
        self.guessed_words = []

        #call the letter input by the user
    

        #create a list with the letters from the secret word
    
        
    def guess_letter(secret_word):

        word_completion = "_" * len(secret_word)
        
        print(word_completion)
        print()

