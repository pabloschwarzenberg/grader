import math

class Vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def norma(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __add__(self,other):
        a = Vector(self.x + other.x,self.y + other.y, self.z + other.z)
        return a
    #def __str__(self):
     #   return '{0},{1},{2}'.format(self.x,self.y,self.z)

def suma_vectores(v1,v2):
    a = Vector(v1.x + v2.x, v1.y + v2.y, v1.z + v2.z)
    return a           