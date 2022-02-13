
class Display:

    """ This class is in charge of displaying the lines and
     organizing the parachute structure
     
    attributes:
    
    methods: """
    
    def __init__(self):
        self.chute = ["\t __","\t/__\\","\t\  /","\t \/"]
        self.life=0
    
    def set_life(self,life):
        self.life=life
        
    def draw(self,life):
        Display.draw_parachute(self,life)
        Display.draw_person(self,life)
        
       
    def draw_person(self,life):
        if self.life>=1:
            print( "\t O")
        else:
            print( "\t X")
        print(" \t/|\\")
        print(" \t/ \\")
      
    def draw_parachute(self,life):
        if self.life==4:
            for j in self.chute:
                print(j)
        else:
            self.chute.pop(0)
            for i in self.chute:
                print(i)

                
                

   
# test1 = Display()

# test1.draw_parachute()

# test1.draw_person()
