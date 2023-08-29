import math
class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def norma(self):
        self.norma=str(self.x**2+self.y**2+self.z**2)
    def __str__(self):
        return norma
def suma_vectores(v1,v2):
    suma=v1+v2
    return suma
if __name__=="__main__":
    vector=Vector()
    x=int(input("Ingrese x: "))
    y=int(input("Ingrese y: "))
    z=int(input("Ingrese z: "))
    v1=int(input("Ingrese v1: "))
    v2=int(input("Ingrese v2: "))
    print("La norma del vector es: ",vector)
    print("La suma de los vectores es: ",suma_vectores(v1,v2))

           