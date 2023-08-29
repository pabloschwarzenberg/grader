class Fraccion:
    def __init__(self,numerador,denominador):
        self.num=numerador
        self.den=denominador

    def __mul__(self,other):
        r=Fraccion(0,0)
        r.num=self.num*other.num
        r.den=self.den*other.den
        return r

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
    def __add__(self, other):
      r=Fraccion(0,0)
      if other.den > self.den:
        if other.den % self.den == 0:
          r.den = other.den
        else:
          r.den = self.den * other.den     
      elif other.den < self.den:
        if self.den % other.den == 0:
          r.den = self.den
        else:
          r.den = self.den * other.den
      else:
        div = other.den
      r.num = (self.num*(r.den//self.den))+(other.num*(r.den//other.den))
      return r
    def __sub__(self, other):
      div = 0
      r=Fraccion(0,0)
      if other.den > self.den:
        if other.den % self.den == 0:
          div = other.den
        else:
          div = self.den * other.den     
      elif other.den < self.den:
        if self.den % other.den == 0:
          div = self.den
        else:
          div = self.den * other.den
      else:
        div = other.den
      r.num = (self.num*(div//self.den))-(other.num*(div//other.den))
      r.den = div
      return r
    def __truediv__(self,other):
      r = Fraccion(0,0)
      r.num = self.num * other.den 
      r.den = self.den * other.num
      return r
    def a_numero(self):
        return self.num/self.den

if __name__ == "__main__":
    f=input("Ingresa la primera fraccion [a/b]: ")
    f=f.split("/")
    f1=Fraccion(int(f[0]),int(f[1]))
    f=input("Ingresa la segunda fraccion [c/d]: ")
    f=f.split("/")
    f2=Fraccion(int(f[0]),int(f[1]))
    print("La suma es ",f1+f2)
    print("La resta es ",f1-f2)
    print("La multiplicación es ",f1*f2)
    print("La división es ",f1/f2)
         