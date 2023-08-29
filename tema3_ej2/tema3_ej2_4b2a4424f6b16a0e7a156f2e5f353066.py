import math
class Vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        self.modulo = ''

    def norma(self):
        self.modulo = (math.sqrt((self.x * 2)+(self.y * 2) + (self.z * 2))) 
    
    def suma_vectores(self):
        pass
    
