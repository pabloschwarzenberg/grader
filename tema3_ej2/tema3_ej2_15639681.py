# crea la clase Vector y completa el código de la función suma_vectores usándola
import math
class Vector:
    def __init__(self,x,y,z):
      self.x=x
      self.y=y
      self.z=z
    def norma(self):
      return math.sqrt((self.x**2)+(self.y**2)+(self.z**2))
      
    def __add__(self,vector):
        return [vector.x+ self.x,vector.y+ self.y, vector.z+ self.z]
        
    def getx(self):
      return self.x
      
    def gety(self):
      return self.y
      
    def getz(self):
      return self.z
    
def suma_vectores(v1,v2):

    v3=Vector(v1.getx()+v2.getx(),v1.gety()+v2.gety(),v1.getz()+v2.getz())

    return v3