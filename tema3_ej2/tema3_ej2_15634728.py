# crea la clase Vector y completa el código de la función suma_vectores usándola
from math import sqrt

class Vector():
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getZ(self):
        return self.z

    def get(self):
        return (self.getX(),self.getY(),self.getZ())
    
    def norma(self):
        return sqrt(self.getX()**2+self.getY()**2+self.getZ()**2)

    def suma_vectores(v,u):
        return Vector(v.getX()+u.getX(),v.getY()+u.getY(),v.getZ()+u.getZ())
    
    def resta(v,u):
        return Vector(v.getX()-u.getX(),v.getY()-u.getY(),v.getZ()-u.getZ())

    def __add__(v,u):
        return Vector.suma_vectores(v,u)

    def __sub__(v,u):
        return Vector.resta(v,u)
def suma_vectores(v,u):
    return Vector(v.getX()+u.getX(),v.getY()+u.getY(),v.getZ()+u.getZ())