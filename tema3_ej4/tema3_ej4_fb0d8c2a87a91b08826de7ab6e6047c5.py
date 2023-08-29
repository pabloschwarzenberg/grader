class Fraccion:
  def __init__(self,numerador,denominador):
      self.num=numerador
      self.den=denominador
      
  def __repr__(self):
        entero = self.num//self.den
        if entero > 0:
            resto = self.num%self.den
            if resto > 0:
                return "{0} {1}/{2}".format(entero,resto,self.den)
            else:
                return "{0}".format(entero)
        else:
            return "{0}/{1}".format(self.num,self.den)
  
  def a_numero(self):
        return self.num/self.den
        
  def __mul__(self,other):
      r=Fraccion(0,0)
      r.num = self.num * other.num
      r.den = self.den * other.den
      return r

  def __add__(self,other):
     self.num = self.num * other.den
     other.num = self.den * other.num
     self.den = self.den * other.den
     other.den = self.den * other.den
     sumafraccion = (self.num + other.num)/self.den
     return sumafraccion
       
  def __sub__(self,other):
     self.num = self.num * other.den
     other.num = self.den * other.num
     self.den = self.den * other.den
     other.den = self.den * other.den
     restafraccion = (self.num - other.num)/self.den
     return restafraccion
       
def operaciones(f1,f2):
  sumarfracciones= f1 + f2
  sumarfracciones.restafracciones
  
         