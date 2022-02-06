from Guess import Guess
from Puzzle import Puzzle
from Display import Display



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
        
        pass

    def star_game(self):
        while self.is_playing:
            self.do_inputs()
            self.check_letter()
            
            
    def do_inputs(self):
        """here is where we ask for a letter.
        
        """
        
        
    def check_letter(self):
        """here is where we have guess check to see if the inputed letter is in the word, then we tell display to add a correct letter into the correct position
        """
        
    def do_output(self):
        """here is where we display the parachute man, the blank word, and a correct letter, or a damaged piece of parachute.
        """