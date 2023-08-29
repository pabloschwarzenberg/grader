# crea la clase Vector y completa el código de la función suma_vectores usándola

class Vector:
          def __init__(self,_x,_y,_z):
                    self.x=_x
                    self.y=_y
                    self.z=_z

          def norma(self):
                    n=((self.x*self.x)+(self.y*self.y)+(self.z*self.z))
                    #print(n)
                    return print("el valor de la norma es ",n**1/2)


          def suma_vectores(self,v2):
                    v=Vector(0,0,0)
                    v.x=self.x+v2.x
                    v.y=self.y+v2.y
                    v.z=self.z+v2.z
                    return v

