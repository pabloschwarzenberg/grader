from math import *
class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def norma(self):
        suma=((self.x)**2)+((self.y)**2)+((self.z)**2)
        resultado=sqrt(suma)
        return resultado

    def __add__(self,other):
        v=Vector(0,0,0)
        v.x=(self.x+other.x)
        v.y=(self.y+other.y)
        v.z=(self.z+other.z)
        return v

def suma_vectores(Vector1,Vector2):
    vec=Vector(0,0,0)
    vec.x=Vector1.x+Vector2.x
    vec.y=Vector1.y+Vector2.y
    vec.z=Vector1.z+Vector2.z
    return vec