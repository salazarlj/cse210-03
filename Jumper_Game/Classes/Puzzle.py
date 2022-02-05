
import random

class Puzzle:
    
    def __init__(self) -> None:
        #needs lots of words in the list
        self.word_list=["dog","tree","horse","coding","gato","hands","elephant","cucumber","pickle","mouse","moose","toenail","blanket","pillow","shirt","glass","door",]
        
        
        
    def get_random_word(self):
        secret_word=random.sample(self.word_list,1)
    
        return secret_word
    
# puzzle=Puzzle()
# Puzzle.get_random_word(puzzle)
