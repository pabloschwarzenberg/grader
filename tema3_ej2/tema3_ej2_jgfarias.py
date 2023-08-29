import math
class Vector:
    x=""
    y=""
    y=""
    """
    Creando metodos
    Sintaxis
    def nombre_Metodo(self):
        acciones
    """
    def mostrarDatos(self):
        print("Coordenada x: ",self.x)
        print("Coordenada y: ",self.y)
        print("Coordenada z: ",self.z)
        print("Vector = [",self.x," ",self.y," ",self.z,"]")
    def norma_del_vector(self):
        x=self.x
        y=self.y
        z=self.z
        norma=math.sqrt((x**2)+(y**2)+(z**2))
        print("La norma del vector es ",norma)

    def __add__(self,other):
        input("Ingrese el primer vector: ")
        x1,x2,x3

def suma():
    x1=int(input("Ingrese la coordenada en x del primer vector: "))
    y1=int(input("Ingrese la coordenada en y del primer vector: "))
    z1=int(input("Ingrese la coordenada en z del primer vector: "))
    print("v1=[",x1," ",y1," ",z1,"]")
    x2=int(input("Ingrese la coordenada en x del segundo vector: "))
    y2=int(input("Ingrese la coordenada en y del segundo vector: "))
    z2=int(input("Ingrese la coordenada en z del segundo vector: "))
    print("v2=[",x2," ",y1," ",z2,"]")
    print("La suma de los vectores v1 y v2 es [",x1+x2," ",y1+y2," ",z1+z2,"]")

vector = Vector()
vector.x = int(input("Ingrese coordenada del vector en el eje x: "))
vector.y = int(input("Ingrese coordenada del vector en el eje y: "))
vector.z = int(input("Ingrese coordenada del vector en el eje z: "))
vector.mostrarDatos()
vector.norma_del_vector()
suma()
           