
import random

class Puzzle:

    """ This class is responsible for creating a random list of words

    attributes:

    methods:
    
    """
    
    def __init__(self) -> None:
        #needs lots of words in the list
        self.word_list=["dog","tree","horse","coding","gato","hands","elephant","cucumber","pickle","mouse","moose","toenail","blanket","pillow","shirt","glass","door",]
        self.word_current = ''
        self.letters_word = []
        
        
    def get_random_word(self):

        # Generate a random word

        secret_word=random.sample(self.word_list,1)
        word_list2 = []
        self.word_current = self.word_list2[secret_word -1]
        #Create a list with the letter from the secret word
        word = self.word_current
        for i in range (len(word)):
            self.letters_word.append(word[i])
    
        return secret_word
    
# puzzle=Puzzle()
# Puzzle.get_random_word(puzzle)
