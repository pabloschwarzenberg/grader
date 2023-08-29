# crea la clase Vector y completa el código de la función suma_vectores usándolcl
#Clase Vector3D
class Vector:
  def __init__(self,x,y,z):
    self.x=x
    self.y=y
    self.z=z
  
  def norma(self):
    a=(self.x)**2
    b=(self.y)**2
    c=(self.z)**2
    return((a+b+c)**(1/2))
  
  def __add__(self,other):
    j=self.x+other.x
    k=self.y+other.y
    l=self.z+other.z
    return Vector(j,k,l)
    
def suma_vectores(v1,v2):
  c1=v1.x+v2.x
  c2=v1.y+v2.y
  c3=v1.z+v2.z
  return Vector(c1,c2,c3) 