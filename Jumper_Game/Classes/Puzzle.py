
import random

class Puzzle:

    """ This class is responsible for creating a random list of words

    attributes:

    methods:
    
    """
    
    def __init__(self):
        #needs lots of words in the list
        self.word_list = ["dog","tree","horse","coding","gato","hands","elephant","cucumber","pickle","mouse","moose","toenail","blanket","pillow","shirt","glass","door",]
        self.secretword = ""
        self.v_temp = ""
    
    def hint_word_list(self):
        self.category = random.randint(1,5)

        self.animal_list = ["cat","bird","bear","butterfly","dog","ant", "elephant", "mouse", "turtle"]    
        self.country_list = ["nicaragua","argentina","united states","mexico","guatemala","costa rica"]    
        self.vehicle_list = ["car","motor cycle","bycicle",""]    
        self.fruit_list = []    
        self.house_list = ["cat","bird","bear","butterfly","dog","ant"]    
        
    def get_random_word(self):

        # Generate a random word

        self.v_temp = random.sample(self.word_list,1)
        self.secretword = self.v_temp[0]
        
        return self.secretword
