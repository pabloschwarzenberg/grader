import math
class Vector:
    def __init__(self,x0 = 0,y0 = 0,z0 = 0):
        self.x = x0
        self.y = y0
        self.z = z0
    def norma(self):
        a = math.sqrt((self.x)**2 + (self.y)**2 + (self.z)**2)
        return a
    def __str__(self):
        b = "({0} {1} {2})".format(self.x,self.y,self.z)
        return b

    def __add__(self, other):
        r = Vector()
        r.x = self.x + other.x
        r.y = self.y + other.y
        r.z = self.z + other.z
        return r
def suma_vectores(v1,v2):
    a = v1 + v2
    return a
