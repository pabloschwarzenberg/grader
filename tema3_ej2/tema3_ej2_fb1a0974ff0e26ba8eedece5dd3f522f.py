import math
class Vector:
    def __init__(self,a,b,c):
        self.x = a
        self.y = b
        self.z = c

    def norma(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __add__(self,other):
        a = self.x + other.x
        b = self.y + other.y
        c = self.z + other.z
        return Vector(a,b,c)
    
def suma_vectores(v1,v2):
    a = v1.x + v2.x
    b = v1.y + v2.y
    c = v1.z + v2.z
    return Vector(a,b,c)
           