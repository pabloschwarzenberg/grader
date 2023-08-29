# crea la clase Vector y completa el código de la función suma_vectores usándola
import math
class Vector:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def norma(self):
        norma=int(((self.a)**(2)+(self.b)**(2)+(self.c)**(2))**(1/2))
        return norma
    
    def __add__(self,t):
        v3=Vector(0,0,0)
        v3.a=self.a+t.a
        v3.b=self.b+t.b
        v3.c=self.c+t.c
        return v3
    
def suma_vectores(h,j):
    f=h+j
    return f