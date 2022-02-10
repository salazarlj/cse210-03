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
        self.secret_word=""
        self.input=""

    def star_game(self):
        while self.is_playing:
            self.do_inputs()
            self.check_letter()
            self.do_output()
            
    def do_inputs(self):
        """here is where we ask for a letter.
        """

        letter=input("guess a letter: ")
        Guess.input=letter
        
    def check_letter(self):
        """here is where we have guess check to see if the inputed letter is in the word, then we tell display to add a correct letter into the correct position
        """
        Guess.guess_letter(Guess())
        Guess.reveal_word(Guess())
        
    def do_output(self):
        """here is where we display the parachute man, the blank word, and a correct letter, or a damaged piece of parachute.
        """
        Display.draw_parachute(Display())
        Display.draw_person(Display())
    
# test1=Game_Master()
# test1.star_game()