
import random

class Puzzle:

    """ This class is responsible for creating a random list of words

    attributes:

    methods:
    
    """
    
    def __init__(self):
        #needs lots of words in the list
        
        self.word_list=[]
        self.word_letters=[]
        self.word=""

    def get_random_word(self):

        self.category = random.randint(1,5)
        cat = self.category
        self.category_list (int(cat))

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

    def category_list(self, category:int):

        self.category = category   
        
        print("\n")
        if category == 1:
            self.word_list = ["dog","horse","gato","elephant","mouse","ant",]
            print ("HINT: THE SECRET WORD IS ABOUT ANIMALS")
        elif category == 2:
            print ("HINT: THE SECRET WORD IS ABOUT FRUITS")
            self.word_list = ["apple","cucumber","banana","strawberry", "watermelon", "mango",]
        elif category == 3:
            print ("HINT: THE SECRET WORD IS ABOUT TYPES OF VEHICLES")
            self.word_list = ["car","train","bus","airplane","bicycle","rocket","door",]
        elif category == 4:
            print ("HINT: THE SECRET WORD IS ABOUT THINGS YOUR HAVE IN YOUR HOUSE")
            self.word_list = ["pillow","shirt","glass","door",]
        else:
            print ("HINT: THE SECRET WORD IS ABOUT AMERICAN COUNTRIES")
            self.word_list = ["nicaragua","argentina","united states","mexico","guatemala",]

# test1=Puzzle()
# test1.get_random_word()

