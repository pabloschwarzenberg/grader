import math
class Vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        x=self.x+other.x
        y=self.y+other.y
        z=self.z+other.z
        return Vector(x,y,z)
    def norma(self):
        x1=(self.x)**2
        y1=(self.y)**2
        z1=(self.z)**2
        return math.sqrt(x1+y1+z1)

def suma_vectores(v1,v2):
    c=v1+v2
    return c
           