# crea la clase Vector y completa el código de la función suma_vectores usándola
class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
        self.v1=[x,y,z]
        self.v2=[x,y,z]
        self.sumavectores=[]

    def suma_vectores(self,v1,v2):
        self.sumavectores.append(self.v1[0]+self.v2[0])
        self.sumavectores.append(self.v1[1]+self.v2[1])
        self.sumavectores.append(self.v1[2]+self.v2[2])
        return self.sumavectores
    
    def norma(self,v1):
        return self.v1[0]*self.v1[0]+self.v1[1]*self.v1[1]+self.v1[2]*self.v1[2]
        
        
        
    
  
           