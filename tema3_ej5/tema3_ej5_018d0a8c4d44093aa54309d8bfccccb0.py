class Ciudad:
    def __init__(self,x,y):
        self.x = x
        self.y = y     
    def __lshift__(self, other):
        if self.x<other.x:
            return True
        if self.y<other.y:
            return True
        else: 
            return False
    def camino(self, other):
        pass
            
    
    def __sub__(self,other):
         xa = self.x - other.x
         ya = self.x - other.y
         return [xa,ya]
    def Ciudad(self,a):
        z = (xa**2 + ya**2)**(1/2)
         