from math import sqrt
class Vector:
    def __init__(self, componenteX, componenteY, componenteZ):
        self.x = componenteX
        self.y = componenteY
        self.z = componenteZ

    def norma(self):
      return sqrt(self.x ** 2 + self.y ** 2 + self.z**2)

    def suma_vectores(self,a):
       return (self.x+a.x,self.y+a.y,self.z+a.z)

if __name__=="__main__":
  a=int(input("Ingrese el valor de la coordenada X1"))
  b=int(input("Ingrese el valor de la coordenada Y1"))
  c=int(input("Ingrese el valor de la coordenada Z1"))
  v1=Vector(a,b,c)
  print("")
  d=int(input("Ingrese el valor de la coordenada X2"))
  e=int(input("Ingrese el valor de la coordenada Y2"))
  f=int(input("Ingrese el valor de la coordenada Z2"))
  v2=Vector(d,e,f)


  print(Vector.suma_vectores(v1,v2))