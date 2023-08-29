import math
class Vector:
   def __init__(self,x,y,z):
     self.x=x 
     self.y=y
     self.z=z
     
   def norma(self):
     norma= math.sqrt(self.x**2 + self.y**2 + self.z**2)
     return norma
     
   def modulo(self):
     return self.norma()
    
   def suma_vectores(self, v1,v2):
     sumax= v1.x + v2.x  
     sumay= v1.y + v2.y
     sumaz= v1.z + v2.z
     Vector3= Vector(sumax,sumay,sumaz)
     return Vector3
     
   def __add__(self, v1):
     c= self.suma_vectores(self,v1)
     return c
       
   
def suma_vectores(v1,v2):
     sumax= v1.x + v2.x  
     sumay= v1.y + v2.y
     sumaz= v1.z + v2.z
     Vector3= Vector(sumax,sumay,sumaz)
     return Vector3
   
  
           