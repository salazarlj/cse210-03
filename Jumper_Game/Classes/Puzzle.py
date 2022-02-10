
import random

class Puzzle:

    """ This class is responsible for creating a random list of words

    attributes:

    methods:
    
    """
    
    def __init__(self):
        #needs lots of words in the list
        self.word_list=["dog","tree","horse","coding","gato","hands","elephant","cucumber","pickle","mouse","moose","toenail","blanket","pillow","shirt","glass","door",]
        self.word_letters=[]
        self.word=""

    def get_random_word(self):

    # Generate a random word
        word_index = random.randint(1, len(self.word_list))
        self.word = self.word_list[word_index-1]
        self.split_word()
 

    def split_word(self):
    # Separates each letter in saving in a list
        word=self.word
        for i in range(len(word)):
            self.word_letters.append(word[i])
        # print(self.word_letters)

    

# test1=Puzzle()
# test1.get_random_word()

