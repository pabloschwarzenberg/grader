# crea la clase Vector y completa el código de la función suma_vectores usándola
class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
        
    def norma(self):
        norma=((self.x*self.x)+(self.y*self.y)+(self.z*self.z))**0.5
        
    def getVector(self):
        vector=[self.x,self.y,self.z]
        return vector
        
def suma_vectores(v1,v2):
  v1=v1.getVector()
  v1=v2.getVector()
  x1=v1[0]
  y1=v1[1]
  z1=v1[2]
  x2=v1[0]
  y2=v1[1]
  z2=v1[2]
  suma=[x1+x2,y1+y2,z1+z2]
  return suma