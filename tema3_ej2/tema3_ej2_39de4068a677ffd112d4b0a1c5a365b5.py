class Vector:

    def __init__(self,v1,v2,v3):
        self.v1=v1
        self.v2=v2
        self.v3=v3

    def norma(self):
        calculo=(self.v1**2+self.v2**2+self.v3**2)**.5
        return calculo

    def __add__(self, other):
        pos1=self.v1+other.v1
        pos2=self.v2+other.v2
        pos3=self.v3+other.v3
        return pos1,pos2,pos3

    def suma_vectores(self,v1,v2):
        suma=self.v1+v2+self.v2+other.v2+self.v3+other.v3
        return suma