# crea la clase Vector y completa el código de la función suma_vectores usándola
class Vector:
    def __init__(self,v1,v2,v3):
        self.v1=v1
        self.v2=v2
        self.v3=v3
        
    def __norma__(self,v1,v2):
        norma = (self.v1**2+self.v2**2)^(1/2)
        return norma
    
    def suma_vectores(v1,v2):
        return self.v1+self.v2
    
    
    