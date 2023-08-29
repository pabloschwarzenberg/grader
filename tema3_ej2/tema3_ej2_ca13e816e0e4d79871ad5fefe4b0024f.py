# crea la clase Vector y completa el código de la función suma_vectores usándola
import math
class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def norma(self):
        a=self.x**2
        b=self.y**2
        c=self.z**2
        s=math.sqrt(a+b+c)
        return s
    def __add__(self, other):
        return Vector((other.x + self.x),(other.y + self.y),(other.z + self.z))
def suma_vectores(x,y):
    return Vector((x.x + y.x), (x.y + y.y), (x.z + y.z))
# >>>>>>>> videos y contenidos del tema 7 NO ESTÁN DISPONIBLES en la plataforma <<<<<<<<