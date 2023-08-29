import math
class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def norma(self):
        d=math.sqrt(self.x**2 + self.y**2 + self.z**2)
        return d
        
    def __add__(self,other):
        x=self.x+other.x
        y=self.y+other.y
        z=self.z+other.z
        return Vector(x,y,z)
        

def suma_vectores(v1,v2):
    return v1+v2
