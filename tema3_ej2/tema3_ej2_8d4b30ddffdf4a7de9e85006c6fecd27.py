# crea la clase Vector y completa el código de la función suma_vectores usándola
class Vector:
    def __init__(self,componentes):
      self.componentes = componentes
    
    def __repr__(self):
      s = ""
      for i in range(len(self.componentes):
        s = s+"{0:<8.2f}".format(self.componentes[i])
        
    def __add__(self,other):
        r =[0]*len(self.componentes)
        d = [0]*len(other.componentes)
        for i in range(len(self.componentes)):
          for j in range(len(other.componentes)):
             r[i] = self.componentes[i] + other.componentes[j]
        return Vector(r)
                    
    
    def suma_vectores(v1,v2):
      v1 = Vector([1,1])
      v2 = Vector([2,2])
      print(v1+v2)
      
      return
           