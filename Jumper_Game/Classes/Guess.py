from Classes.Puzzle import Puzzle
class Guess:

    """This class is in charge of the player´s guessing letter part

    attributes:

    methods:

    """

    def __init__(self):

        #choose a random word
        Guess.secret_word = Puzzle.get_random_word(Puzzle())

        #call the letter input by the user
        Guess.input = ""

        #create a list with the letters from the secret word
        Guess.secrets_letters = [x for x in Guess.secret_word]

    def guess_letter(self):
        #compare the letter inputed with the letters in the list

        if Guess.input in Guess.secrets_letters:
            for i in range(len(Guess.secrets_letters)):
                if Guess.input == Guess.secrets_letters:
                    return Guess.secrets_letters #return the letter if this is in the list
                else:
                    return False  

    def reveal_word(self):
        #call the letter if this exist in the list or draw a dashes if there isn't
        reveal_letter = Guess.guess_letter(Guess.secrets_letters)
        if reveal_letter == True:
            print(reveal_letter)
        else:
            print("_")
        
