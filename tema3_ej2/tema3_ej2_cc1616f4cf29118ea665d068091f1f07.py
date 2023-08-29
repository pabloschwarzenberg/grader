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
        # Configurar el método especial __add__ para que el operador +
        # pueda sumar dos vectores en el espacio R3
        vs = Vector(0,0,0) # vector suma
        vs.x = self.x + other.x
        vs.y = self.y + other.y
        vs.z = self.z + other.z
        return vs
      
# crea la clase Vector y completa el código de la función suma_vectores usándola
def suma_vectores(v1,v2):
    vs = Vector(0,0,0) # vector suma
    vs = v1 + v2
    return vs           