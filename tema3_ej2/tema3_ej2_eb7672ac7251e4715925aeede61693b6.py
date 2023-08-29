# crea la clase Vector y completa el código de la función suma_vectores usándola
class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __str__(self):
        return "({0},{1},{2})".format(self.x,self.y,self.z)
    def norma(self):
        a = (float(self.x)**2 + float(self.y)**2 + float(self.z)**2)**(1/2)
        return a
    def __add__(self,other):
        self.x=self.x+other.x
        self.y=self.y+other.y
        self.z=self.z+other.z
        return self

def suma_vectores(v1,v2):
  return v1+v2
