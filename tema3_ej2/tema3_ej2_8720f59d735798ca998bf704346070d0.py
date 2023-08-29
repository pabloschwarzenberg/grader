import math
class Vector:
    def __init__(self,x,y,z):
        self.x=float(x)
        self.y=float(y)
        self.z=float(z)

    def __str__(self):
        return "({},{},{})".format(self.x,self.y,self.z)
    def norma(self):
        norma=float(math.sqrt((self.x**2)+(self.y**2)+(self.z**2)))
        return norma
    def __add__(self,otro):
        r=suma_vectores(self, otro)
        return r
def suma_vectores(v1,v2):
    r=Vector(0,0,0)
    r.x=v1.x+v2.x
    r.y=v1.y+v2.y
    r.z=v1.z+v2.z
    return r

         