import math

class Vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def norma(self):
        return math.sqrt(self.x**2+self.y**2+self.z**2)
    def __add__(self,other):
        v3x = self.x + other.x
        v3y = self.y + other.y
        v3z = self.z + other.z
        v3 = Vector(v3x, v3y, v3z)
        return v3

def suma_vectores(v1,v2):
        return v1+v2

v1=Vector(2,2,2)
v2=Vector(3,1,2)
v1+v2
