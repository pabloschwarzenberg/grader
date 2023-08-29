# crea la clase Vector y completa el código de la función suma_vectores usándola
import math
class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def norma(self):
        n=math.sqrt(self.x*self.x+self.y*self.y+self.z*self.z)
        return n
    def suma_vectores(self,other):
        suma_x=self.x + other.x
        suma_y=self.y + other.y
        suma_z=self.z + other.z
        return(suma_x,suma_y,suma_z)