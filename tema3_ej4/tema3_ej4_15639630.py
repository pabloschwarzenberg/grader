class Fraccion:
    def __init__(self,numerador,denominador):
        self.num=numerador
        self.den=denominador

    def __mul__(self,b):
        r=Fraccion(0,0)
        r.num=self.num*b.num
        r.den=self.den*b.den
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

    def a_numero(self):
        return self.num/self.den
    
    def suma(self,b):
      r=Fraccion(0,0)
      if self.num==b.num:
        r.num=b.num + self.num
        r.den=self.den
      else:
        r.num=(self.num*b.den)+(b.num*self.den)
        r.den=self.den*b.den 
      return r
    
    def resta(self,b):
      r=Fraccion(0,0)
      if self.num==b.num:
        r.num=b.num - self.num
        r.den=self.den
      else:
        r.num=(self.num*b.den)-(b.num*self.den)
        r.den=self.den*b.den 
      return r
      
    def division(self,b):
      r=Fraccion(0,0)
      r.num=self.num*b.den
      r.den=self.den*b.num
      return r
    

if __name__ == "__main__":
    f=input("Ingresa la primera fraccion [a/b]: ")
    f=f.split("/")
    f1=Fraccion(int(f[0]),int(f[1]))
    f=input("Ingresa la segunda fraccion [c/d]: ")
    f=f.split("/")
    f2=Fraccion(int(f[0]),int(f[1]))
    print("La suma es ",Fraccion.suma(f1,f2))
    print("La resta es ",Fraccion.resta(f1,f2))
    print("La división es ",Fraccion.division(f1,f2))
         