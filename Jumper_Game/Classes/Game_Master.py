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
        self.user_input = ""
        self.guessed = False
        self.tries = 6
        self.guessed_letters = []
        self.guessed_words = []
        self.word = Puzzle.get_random_word(Puzzle())
        self.word_completion = Guess.guess_letter(Guess())
       
        pass

    def star_game(self):
        while self.is_playing:
            self.do_inputs()
            self.do_output()
            
            
    def do_inputs(self):
        """here is where we ask for a letter.
        
        """

        while not self.is_playing ==False and self.tries > 0:

            user_input = input("guess a letter [a-z]: ").upper()

            if len(user_input) == 1 and user_input.initial():

                if user_input in self.guessed_letters:
                    print("You already guessed the letter", user_input)
                elif user_input not in self.guessed_letters:
                    print(user_input, "is not in the word")
                    self.tries -= 1
                    self.guessed_letters.append(user_input)
                else:
                    print("Good job!", user_input, "is the word!")
                    self.guessed_letters.append(user_input)
                    word_as_list = list(self.word_completion)
                    indices = [i for i, letter in enumerate(self.word) if letter == user_input]
                    for index in indices:
                        word_as_list[index] = user_input
                    self.word_completion = "".join(word_as_list)
                    if "_" not in self.word_completion:
                        self.guessed = True
            elif len(user_input)== len(self.word) and self.initial():
                if user_input in self.guessed_words:
                    print("You already guessed the word!", user_input)
                elif user_input != self.word:
                    print(user_input, "is not the word")
                    self.tries -= 1
                    self.guessed_words.append(user_input)
                else:
                    self.guessed = True 
                    self.word_completion = self.word
            else:
                print("Not a valid guess.")
                self.is_playing == True
        if self.guessed:
            print("Congrats you win!")
        else:
            print("Sorry, you can play it again!")

    def do_output(self):
        """here is where we display the parachute man, the blank word, and a correct letter, or a damaged piece of parachute.
        """
        Display.draw_parachute(Display())
    