def suma_vectores(v1,v2):
  return
class Vector:
    def __init__(self,a,b,c):
        self.x = a
        self.y = b
        self.z = c

    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+","+str(self.z)+")"

    def norma(self):
        n = (self.x*2 + self.y*2 + self.z*2)*(1/3)
        return round(n,0)

    def __add__(self,other):
        vs = Vector(0,0,0)
        vs.x = self.x + other.x
        vs.y = self.y + other.y
        vs.z = self.z + other.z
        return vs

# Función suma_vectores
def suma_vectores(v1,v2):
    vs = Vector(0,0,0)
    vs = v1 + v2
    return vs    

#Clase fraccion
class Fraccion:
    def __init__(self,numerador,denominador):
        self.num=numerador
        self.den=denominador

    def __mul__(self,other):
        m=Fraccion(0,0)
        m.num=self.num*other.num
        m.den=self.den*other.den
        return m
    
    def __truediv__(self, other):
        d = Fraccion(0,0)
        d.num=self.num/(1/other.den)
        d.den=self.den/(1/other.num)
        return d
    
    def __sub__(self,other):
        r=Fraccion(0,0)
        r.num=(self.num*other.den)-(self.den*other.num)
        r.den=self.den*other.den
        return r
    
    def __add__(self,other):
        m=Fraccion(0,0)
        m.num=(self.num*other.den)+(self.den*other.num)
        m.den=self.den*other.den
        return m
      
    def __repr__(self):
        entero=self.num//self.den
        if entero>0:
            resto=self.num%self.den
            if resto>0:
                return "{0} {1}/{2}".format(entero,resto,self.den)
            else:
                return "{0}".format(entero)
        else:
            return "{0}/{1}".format(self.num,self.den)