
class Display:

    """ This class is in charge of displaying the lines and
     organizing the parachute structure
     
    attributes:
    
    methods: """
    
    def __init__(self):
        self.chute = ["\t __","\t/__\\","\t\  /","\t \/"]
        self.life=4
        
    def draw(self):
        Display.draw_person()
        Display.draw_parachute()
       
    def draw_person(self):
        if self.life>0:
            print( "\t O")
        else:
            print( "\t X")
        print(" \t/|\\")
        print(" \t/ \\")
      
    def draw_parachute(self):
        if self.life==4:
            for j in self.chute:
                print(j)
        elif self.life==3:
            for i in range(1):
                self.chute.pop(0)
            for i in self.chute:
                print(i)
        elif self.life==2:
            for i in range(2):
                self.chute.pop(0)
            for i in self.chute:
                print(i)
        elif self.life==1:
            for i in range(3):
                self.chute.pop(0)
            for i in self.chute:
                print(i)
        else:
            pass
                
                

   
# test1 = Display()

# test1.draw_parachute()

# test1.draw_person()
