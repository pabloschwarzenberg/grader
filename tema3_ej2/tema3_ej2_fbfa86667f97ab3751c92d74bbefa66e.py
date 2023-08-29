class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        v1 = self.x + self.y + self.z 
        
    def norma(v1):
        norma = v1**(1/2)
        return norma
        
    def  __add__(self,other):
        return(self.x + other.x, self.y + other.y, self.z + other.z)