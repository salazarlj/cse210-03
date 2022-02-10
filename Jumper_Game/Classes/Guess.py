from Puzzle import Puzzle
from Game_Master import Game_Master


class Guess:

    """This class is in charge of the player´s guessing letter part

    attributes:

    methods:

    """

    def __init__(self):
# <<<<<<< victor-daniel-gauna
# =======
#         secret_word=Puzzle.get_random_word(Puzzle())
#         print(secret_word)
    
#     def guess_letter():
#         pass
#     def reveal_word():
#         pass
# >>>>>>> main

        #choose a random word
        secret_word = Puzzle.get_random_word(Puzzle())

        #call the letter input by the user
        inputs = Game_Master.do_inputs

        #create a list with the letters from the secret word
        secrets_letters = []
        for i in range(len(self.secret_word)):
            self.secrets_letters.append(secret_word[i])
        
        return secrets_letters

    def guess_letter(self):
        #call the list with the secrets letters
        guessed = self.secrets_letters

        #compare the letter inputed with the letters in the list
        if self.inputs in  self.guessed:
            for i in range(len(self.guessed)):
                if self.inputs == self.guesssed[i]:
                    return guessed #return the letter if this is in the list
                else:
                    return False  

# <<<<<<< victor-daniel-gauna
#     def reveal_word(self):
#         #call the letter if this exist in the list or draw a dashes if there isn't
#         reveal_letter = self.guess_letter()
#         if reveal_letter:
#             print(reveal_letter)
#         else:
#             print("_")
        
# =======
# guess=Guess()
# >>>>>>> main
