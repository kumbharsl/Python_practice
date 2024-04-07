class BCCI:
    def __init__(self):
        print('Board Cricket Council of India')
        
    def captain(self):
        print('Cricket team Captain')
    
class IPL(BCCI):
    def __init__(self):
        #print('India Premear Leage')
        pass
        super().__init__()
        
        
    def team(self):
        print('India team')
        
obj1 = IPL()
obj1.captain()
obj1.team()
    