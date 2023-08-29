class Vector:
    def __init__(self,componentes):
        self.componentes=componentes

    def __add__(self,otro):
        r=[0]*len(self.componentes)
        for i in range(len(self.componentes)):
            r[i]=self.componentes[i]+otro.componentes[i]
        return Vector(r)
        
    def norma(self,otro):

print(v1+v2)
           