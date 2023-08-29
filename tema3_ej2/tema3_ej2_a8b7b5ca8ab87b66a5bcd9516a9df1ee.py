class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
        self.norma=0
    
    def norma(self):
        self.norma=(self.x^2+self.y^2+self.z^2)^(1/2)
    
    def __add__(self,v):
        sumax= self.x + v.x
        sumay = self.y + v.y
        sumaz = self.z + v.z
        vectorsuma=Vector(sumax, sumay, sumaz)
        return vectorsuma
     

# crea la clase Vector y completa el código de la función suma_vectores
# usándola
def suma_vectores(v1,v2):
    SumaVectores=v1.__add__(v2)
    
    return SumaVectores


