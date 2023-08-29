# crea la clase Vector y completa el código de la función suma_vectores usándola
import math
class Vector:
    def __init__(self,x=0,y=0,z=0):
        self.x=x
        self.y=y
        self.z=z
    def set_x(self,x):
        self.x=x
    def set_y(self,y):
        self.y=y
    def set_z(self,z):
        self.z=z
    def norma(self):
        norma=math.sqrt((self.x)**2+(self.y)**2+(self.z)**2)
        return norma
    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+","+str(self.z)+")"
    def __add__(self,v2):
        xf=self.x+v2.x
        yf=self.y+v2.y
        zf=self.z+v2.z
        vf=Vector()
        vf.set_x(xf)
        vf.set_y(yf)
        vf.set_z(zf)
        return vf
def suma_vectores(v1,v2):
        xf=v1.x+v2.x
        yf=v1.y+v2.y
        zf=v1.z+v2.z
        vf=Vector()
        vf.set_x(xf)
        vf.set_y(yf)
        vf.set_z(zf)
        return vf
if __name__=="__main__":
  vector=Vector()
  vector.set_x(int(input("Ingresa la primera coordenada del vector: ")))
  vector.set_y(int(input("Ingresa la segunda coordenada del vector: ")))
  vector.set_z(int(input("Ingresa la tercera coordenada del vector: ")))
  print("La norma del vector",vector,"es",vector.norma())
  v2=Vector()
  v2.set_x(int(input("Ingresa la primera coordenada de un segundo vector: ")))
  v2.set_y(int(input("Ingresa la segunda coordenada de un segundo vector: ")))
  v2.set_z(int(input("Ingresa la tercera coordenada de un segundo vector: ")))