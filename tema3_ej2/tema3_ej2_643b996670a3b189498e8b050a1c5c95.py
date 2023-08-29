# crea la clase Vector y completa el código de la función suma_vectores usándola
class vectores:
    def __init__(self,v1,v2):
        self.v1=v1
        self.v2=v2

    def suma_vectores(v1,v2):
        v3=""
        int(v1[0])+int(v2[0])=v3[0]
        int(v1[2])+int(v2[2])=v3[2]
        int(v1[4])+int(v2[4])=v3[4]
        return v3
        
    def norma(v):
        v[0]=int(v[0])**2
        v[2]=int(v[2])**2
        v[4]=int(v[4])**2
        vn=(v[0]+v[1]+v[2])**1/2
        return vn
       
  
           