from Classes.Guess import Guess
from Classes.Puzzle import Puzzle
from Classes.Display import Display



class Game_Master:

    """ This class is responsible for organizing the game Jumper
    attributes:
    
    methods:

    """
    def __init__(self):
        
        self.is_playing=True
        self.guess=Guess()
        self.puzzle=Puzzle()
        self.display=Display()
        self.input=""
        self.word_letters=self.puzzle.word_letters
        self.secret_letters=[]
        self.life=self.guess.life
        self.word=self.puzzle.word
    
    def start_game(self,):
        self.word=self.puzzle.get_random_word()
        self.guess.set_word_letters(self.word_letters)
        self.display.set_life(self.life)
        self.guess.set_secret_letters(self.secret_letters)

        for i in range(len(self.puzzle.word_letters)):
          self.secret_letters.append('_')
     
        while self.is_playing:
            
            print("  ".join(self.secret_letters))
            print()
            
            self.display.draw(self.life)
            print()
            
            # cat = Puzzle.category_list.
            self.input=input("guess a letter: ") 
            if self.guess.guess_letter(self.input)== False:
                self.life-=1
            self.display.set_life(self.life)
            
            
            if self.word_letters==self.secret_letters:
                print("Congrats! You Won!")
                self.is_playing==False
                break
            
            if self.life<1:
                self.display.draw(self.life)
                print("YOU DIED!!")
                self.is_playing==False
                break
                
            
        
    
            
