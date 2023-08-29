from math import sqrt
class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    
    def norma(self):
        norma = sqrt((self.x**2)+(self.y**2)+(self.z**2))
        return norma
    
    def __add__(self, other):
        x = self.x+other.x
        y = self.y+other.y
        z = self.z+other.z
        c = Vector(x,y,z)
        return c

def suma_vectores(v1, v2):
    v3 = v1+v2
    return v3
           