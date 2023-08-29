# crea la clase Vector y completa el código de la función suma_vectores usándola
class Vector:
        def __init__(self,x,y,z):
          self.x=int(x)
          self.y=int(y)
          self.z=int(z)
        def norma(self):
          self.norma=((self.x*self.x)+(self.y*self.y)+(self.z*self.z))**(1/2)
          return self.norma

def suma_vectores(v1,v2):
    v3_x=v1.x+v2.x
    v3_y=v1.y+v2.y
    v3_z=v1.z+v2.z
    return Vector(v3_x,v3_y,v3_z)
    
    
    
    
    
    
    
        
           