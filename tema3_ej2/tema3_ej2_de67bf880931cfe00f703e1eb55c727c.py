import math

class Vector:
    def __init__(self,x,y,z):
        self.x=float(x)
        self.y=float(y)
        self.z=float(z)
    def __str__(self):
        return "({},{},{})".format(self.x,self.y,self.z)       
    def norma(self):
        norma = float(math.sqrt((self.x**2)+(self.y**2)+(self.z**2)))
        return norma     
    def __add__(self,other):
        f = suma_vectores(self,other)
        return f
def suma_vectores(v1,v2):
    f=Vector(0,0,0)
    f.x=v1.x + v2.x
    f.y=v1.y + v2.y
    f.z=v1.z + v2.z
    return f

           