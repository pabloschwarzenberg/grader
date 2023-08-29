class Fraccion:
    def __init__(self,num,den):
      if isinstance (num, int):
          self.num = num
      else:
          self.num = 0
      if isinstance (den, int) and den !=0:
          self.den = den
      else:
          self.den = 1
            
    def __mul__(self,other):
        r.num=self.num*other.num
        r.den=self.den*other.den
        r=Fraccion(0,0)
        return r
    
    def __add__(self,other):
        num=self.num*other.den + self.den * other.num
        den=self.den*other.den
        r=Fraccion(0,0)
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
         