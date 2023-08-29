import math
class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def __add__(self,other):
        a=Vector(0,0,0)
        a.x=self.x+other.x
        a.y=self.y+other.y
        a.z=self.z+other.z
        return a
    def norma (self):
        norma= math.sqrt((self.x**2)+(self.y**2)+(self.z**2))
        return norma
        
      
    
    
    
def suma_vectores(v1,v2):
    s=v1+v2
    return s
  
           