from math import sqrt
class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __add__(self,other):
        x=self.x+other.x
        y=self.y+other.y
        z=self.z+other.z
        r=Vector(x,y,z)
        return r
    def norma(self):
        n=(self.x**2)+(self.y**2)+(self.z**2)
        norma=sqrt(n)
        return norma
def suma_vectores(v1,v2):
    c=v1+v2
    return c
           