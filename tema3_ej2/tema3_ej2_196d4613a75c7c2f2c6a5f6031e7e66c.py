# crea la clase Vector y completa el código de la función suma_vectores usándola
def suma_vectores(v1,v2):
  return
class Vector:
    def __init__(self,a,b,c):
        self.x = a
        self.y = b
        self.z = c

    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+","+str(self.z)+")"

    def norma(self):
        n = (self.x*2 + self.y*2 + self.z*2)*(1/3)
        return round(n,0)

    def __add__(self,other):
        vs = Vector(0,0,0)
        vs.x = self.x + other.x
        vs.y = self.y + other.y
        vs.z = self.z + other.z
        return vs

# Función suma_vectores
def suma_vectores(v1,v2):
    vs = Vector(0,0,0)
    vs = v1 + v2
    return vs           
           