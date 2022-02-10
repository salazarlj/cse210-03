from Classes.Display import Display
class Guess:

    """This class is in charge of the player´s guessing letter part

    attributes:

    methods:

    """

    def __init__(self):

        self.word_letters=[]
        self.secret_letters=[]
        self.input=""
        self.display=Display()
        self.life=4





    def set_word_letters(self,list):
        self.word_letters=list
        
    def set_secret_letters(self,list):
        self.secret_letters=list
        
    def set_input(self,input):
        self.input=input
           
    def guess_letter(self,input):
        #compare the letter inputed with the letters in the list

        if input in self.word_letters:
            for i in range(len(self.word_letters)):
                if input == self.word_letters[i]:
                   self.secret_letters[i] = input
                
        else:
            return(False)

        
# test1=Guess()
# words=test1.guess_letter
# print()
# print(words)
