import math
class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def norma(self):
        norma=((self.x**2)+(self.y**2) + self.z**2)**(0.5)
        return norma

    def __add__(self, other):
        suma=Vector(0,0,0)
        suma.x=self.x + other.x
        suma.y=self.y + other.y
        suma.z=self.z + other.z
        return suma

def suma_vectores(v1,v2):
    sum=v1+v2
    return sum
           