from math import sqrt

class Vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def norma(self):
        n = (self.x ** 2) + (self.y ** 2) + (self.z ** 2)
        n = sqrt(n)
        return n

    def __add__(self,other):
        if isinstance(other,Vector):
            return suma_vectores(self,other)
        else:
            pass

def suma_vectores(self,other):
    x = self.x + other.x
    y = self.y + other.y
    z = self.z + other.z
    t = Vector(x,y,z)
    return t