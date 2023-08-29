# crea la clase Vector y completa el código de la función suma_vectores usándola
import math

class Vector:
    def __init__(self, x,y,z):
        self.x=x
        self.y=y
        self.z=z
    
    ### Metodos
    def norma(self):
        norma=(self.x**2)+(self.y**2)+(self.z**2)
        self.norma1=math.sqrt(norma)
        return self.norma1
    
    def __add__(self, v2):
       return suma_vectores(self, v2)
    
    def __str__(self):
        return "{0},{1},{2}".format(self.x,self.y,self.z)
        
def suma_vectores(v1,v2):
        r=Vector(0,0,0)
        r.x=(v1.x + v2.x)
        r.y=(v1.y + v2.y)
        r.z=(v1.z + v2.z)
        return r