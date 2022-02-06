class Display:
    
   """ This class is in charge of displaying the lines and
     organizing the parachute structure
     
    attributes:
    
    methods:"""
    
     def __init__(self):
        self.space = " "
       
    def draw_person(self):
        print("\t"+self.space+"O")
        print("\t/|\\")
        print("\t/ \\")
      
    def draw_parachute(self):
        print ("\t"+self.space+"__")
        print("\t/__\\")
        print("\t\  /")
        print("\t \/")
   
test1 = Display()

test1.draw_parachute()

test1.draw_person()