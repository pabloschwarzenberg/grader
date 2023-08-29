import math
class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def norma(self):
        norma = math.sqrt(self.x**2+self.y**2+self.z**2)
        return norma
        return suma_x,suma_y,suma_z
    def __add__(self,other):
        resultado=Vector(0,0,0)
        resultado.x=self.x+other.x
        resultado.y=self.y+other.y
        resultado.z=self.z+other.z
        return resultado
    def __repr__(self):
        return str(self.x)+","+str(self.y)+","+str(self.z)
def suma_vectores(v1,v2):
    resultado=Vector(0,0,0)
    resultado.x=v1.x+v2.x
    resultado.y=v1.y+v2.y
    resultado.z=v1.z+v2.z
    return resultado