
import random

class Puzzle:

    """ This class is responsible for creating a random list of words

    attributes:

    methods:
    
    """
    
    def __init__(self) -> None:
        #needs lots of words in the list
        self.word_list=["dog","tree","horse","coding","gato","hands","elephant","cucumber","pickle","mouse","moose","toenail","blanket","pillow","shirt","glass","door",]
     
    def get_random_word(self):

        # Generate a random word

        secret_word = random.sample(self.word_list)
        
        return secret_word.upper()
        
