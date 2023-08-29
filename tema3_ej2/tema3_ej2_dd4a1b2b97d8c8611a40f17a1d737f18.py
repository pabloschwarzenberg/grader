# crea la clase Vector y completa el código de la función suma_vectores usándola

import math
class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __repr__(self):
        vector="["+str(self.x)+","+str(self.y)+","+str(self.z)+"]"
        return vector
    def norma(self):
        x2=self.x**2
        y2=self.y**2
        z2=self.z**2
        add=x2+y2+z2
        norm=math.sqrt(add)
        return norm
        
    def __add__(self,otro):
        sumx=self.x+otro.x
        sumy=self.y+otro.y
        sumz=self.z+otro.z
        x=Vector(self.x+otro.x,self.y+otro.y,self.z+otro.z)
        return x

def suma_vectores(v1,v2):
    return v1+v2
