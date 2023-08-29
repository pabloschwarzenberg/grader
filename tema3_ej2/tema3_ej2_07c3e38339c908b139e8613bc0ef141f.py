# crea la clase Vector y completa el código de la función suma_vectores usándola
class Vector:
  def __init__(self,x,y,z):
    self.x=x
    self.y=y
    self.z=z
  def norma(self):
    norma = ((self.x)**2 + (self.y)**2 + (self.z)**2)**(1/2)
    return norma
    
  def __add__(self,valor):
      r=Vector(0,0,0)
      r.x=self.x+valor.x
      r.y=self.y+valor.y
      r.z=self.z+valor.z
      return r

def suma_vectores(v1,v2):
  resultado = v1+v2
  return resultado
           