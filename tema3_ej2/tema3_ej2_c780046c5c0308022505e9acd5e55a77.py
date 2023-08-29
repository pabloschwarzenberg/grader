# crea la clase Vector y completa el código de la función suma_vectores usándola
class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
        
    def norma(self):
        norma=((self.x**2)+(self.y**2)+(self.z**2))**(1/2)
        return norma
        
    def __add__(self,other):
        x_s=self.x+other.x
        y_s=self.y+other.y
        z_s=self.z+other.z
        v_r=Vector(x_s,y_s,z_s)
        return v_r
        
def suma_vectores(v1,v2):
   x_suma=v1.x+v2.x
   y_suma=v1.y+v2.y
   z_suma=v1.z+v2.z
   v_resultante=Vector(x_suma,y_suma,z_suma)
   return v_resultante
    

        
        