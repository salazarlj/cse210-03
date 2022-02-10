from Classes.Puzzle import Puzzle
class Guess:

    """This class is in charge of the player´s guessing letter part

    attributes:

    methods:

    """

    def __init__(self):

        #choose a random word
        Guess.secret_word =Puzzle.get_random_word(Puzzle())
        self.word_letters = []
        #call the letter input by the user
        #Guess.input = "" 

        #create a list with the letters from the secret word

        word = Guess.secret_word

        for i in range(len(word)):
            self.word_letters.append(word[i])


        Guess.secrets_letters = [x for x in Guess.secret_word]

    def guess_letter(self):
        #compare the letter inputed with the letters in the list
        if Guess.input=="":
            print("input is blank")
        else:
            print(Guess.input)
        if Guess.secret_word=="":
            print("secret word is blank")
        print("the word is")
        print(Guess.secret_word)
        print("the letters are")
        print(Guess.secrets_letters)
        print (len(Guess.secrets_letters))
        if Guess.input in Guess.secrets_letters:
            for i in range(len(Guess.secrets_letters)):
                if Guess.input == Guess.secrets_letters[i]:
                    return Guess.secrets_letters #return the letter if this is in the list
                else:
                    return False  

    def reveal_word(self):
        #call the letter if this exist in the list or draw a dashes if there isn't
        reveal_letter = Guess.guess_letter(Guess())
        if reveal_letter:
            print(reveal_letter)
        else:
            print("_")
        
# test1=Guess()
# words=test1.guess_letter
# print()
# print(words)
