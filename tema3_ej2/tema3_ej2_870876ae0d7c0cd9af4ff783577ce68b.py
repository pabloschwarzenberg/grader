import math
class Vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def norma(self):
        n = self.x**2+self.y**2+self.z**2
        return math.sqrt(n)
    def __add__(self,other):
        v = Vector(0,0,0)
        v.x = self.x + other.x
        v.y = self.y + other.y
        v.z = self.z + other.z
        return v
def suma_vectores(v1,v2):
    v3=v1+v2
    return v3