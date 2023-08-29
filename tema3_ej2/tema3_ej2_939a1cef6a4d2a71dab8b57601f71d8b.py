# crea la clase Vector y completa el código de la función suma_vectores usándola
# crea la clase Vector y completa el código de la función suma_vectores usándola
class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
        self.modulo=None

    def norma(self):
        self.modulo=((self.x**2)+(self.y**2)+(self.z**2))**(1/2)
        print(self.modulo)

    def suma_vectores(self,v1,v2):
        suma_x=v1.x+v2.x
        suma_y=v1.y+v2.y
        suma_z=v1.z+v2.z
        suma=Vector(suma_x,suma_y,suma_z)
           