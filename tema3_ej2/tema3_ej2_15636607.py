# crea la clase Vector y completa el código de la función suma_vectores usándola
class Vector:
  def componentes(self,x,y,z):
    self.x=x
    self.y=y
    self.z=z
  def norma_vector(self,vector):
    norma=((((((self.x)**2)+(self.y**2))**(1/2))**2)+self.z**2)**(1/2)
    return(norma,a)
  def __init__(self,x,y,z,norma)
    self.x=x
    self.y=y
    self.z=z
    self.norma=norma
def suma_vectores(v1,v2):
  xf=v1.x+v2.x
  yf=v1.y+v2.y
  zf=v1.z+v2.z
  return(xf,yf,zf)
norma0=0 
if __name__ == "__main__":
  a=Vector((int(input("Componente x:"))),(int(input("Componente y:"))),(int(input("Componente z:"))))
  b=Vector((int(input("Componente x:"))),(int(input("Componente y:"))),(int(input("Componente z:"))))
  print(a.norma_vector(a))
  print(b.norma_vector(b))
  print(suma_vectores(a,b))
