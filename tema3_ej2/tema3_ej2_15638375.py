# crea la clase Vector y completa el código de la función suma_vectores usándola
class Vector():
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def suma_vectores(self,v):
        a=self.x+v.x
        b=self.y+v.y
        c=self.z+v.z
        return '('+str(a)+','+str(b)+','+str(c)+')'
    def norma(self):
        norma=(self.x**2+self.y**2+self.z**2)**(1/2)
        return norma
    def __add__(self,v):
        a=self.x+v.x
        b=self.y+v.y
        c=self.z+v.z
        return '('+str(a)+','+str(b)+','+str(c)+')'