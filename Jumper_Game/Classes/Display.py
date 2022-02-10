
from Jumper_Game.Classes.Guess import Guess


class Display:

    """ This class is in charge of displaying the lines and
     organizing the parachute structure
     
    attributes:
    
    methods: """
    
    def __init__(self):
        self.tries = 6

       
    def draw_parachute(self):
        stages = [
            """"_________
				 |	 |
				 |	 O
				 |	\|/
				 |	 |
				 |	/ \ 
				 |________""",

                 """
                 _________
				 |	 |
				 |	 O
				 |	\|/
				 |	 |
				 |
				 |________
                 """,

                 """"
                 _________
				 |	 |
				 |	 O
				 |	\|
				 |	 |
				 |
				 |________""",

                 """"
                 ________
				 |	 |
				 |	 O
				 |	 |
				 |	 |
				 |
				 |________""",
                 """
                  _________
				 |	 |
				 |	 O
				 |
				 |
				 |
				 |________
                 """,
                """
				 _________
				 |	 |
				 |
				 |
				 |
				 |
				 |________
				"""
        ]
        return stages[self.tries]
				 
		 
				 
		 
			
		 
		 
				 
				 
        
            
