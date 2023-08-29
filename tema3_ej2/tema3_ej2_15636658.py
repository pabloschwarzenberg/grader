import math
class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def norma (self):
        resultado=math.sqrt(self.x**2+self.y**2+self.z**2)
        return resultado

        
    def __add__(self,otro):
        x=self.x+otro.x
        y=self.y+otro.y
        z=self.z+otro.z
        resultado=Vector(x,y,z)
        return  resultado
    def __repr__(self):
        return str(self.x)+","+str(self.y)+","+str(self.z)

def suma_vectores(v1,v2):
        x=v1.x+v2.x
        y=v1.y+v2.y
        z=v1.z+v2.z
        resultado=Vector(x,y,z)
        return resultado




