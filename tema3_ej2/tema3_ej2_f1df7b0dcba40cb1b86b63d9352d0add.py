# crea la clase Vector y completa el código de la función suma_vectores usándola
class vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def norma(self):
        n=(self.x**2+self.y**2+self.z**2)**(1/2)
        return n

def suma_vectores(v1,v2):
    v3=vector(0,0,0)
    v3.x=v1.x+v2.x
    v3.y=v1.y+v2.y
    v3.z=v1.z+v2.z
    return v3