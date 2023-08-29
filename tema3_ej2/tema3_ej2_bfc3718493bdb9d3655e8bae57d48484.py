# crea la clase Vector y completa el código de la función suma_vectores usándola
class Vector:
    def __init__(self,a,b,c):
        self.x = a
        self.y = b
        self.z = c

    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+","+str(self.z)+")"

    def norma(self):
        n = (self.x**2 + self.y**2 + self.z**2)**(1/2)
        return round(n,2)

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


v1 = Vector(1,2,3)
print("Vector 1: ",v1," Norma: ",v1.norma())
v2 = Vector(2,2,2)
print("Vector 2: ",v2," Norma: ",v2.norma())
print("Suma de ",v1," y ",v2," = ",suma_vectores(v1,v2))
