from math import *
class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def norma(self):
        norma=sqrt(self.x**2+self.y**2+self.z**2)
        return norma
    def __add__(self,other):
        x_t=self.x+other.x
        y_t=self.y+other.y
        z_t=self.z+other.z
        c=(x_t,y_t,z_t)
        return c
def suma_vectores(v1,v2):
    x=v1.x+v2.x
    y=v1.y+v2.y
    z=v1.z+v2.z
    return (x,y,z)
