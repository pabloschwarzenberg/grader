class Fraccion:
    def __init__(self,numerador,denominador):
        self.num=numerador
        self.den=denominador
    def __add__(self,other):
        fadd=Fraccion(0,0)
        if self.den==other.den:
          fadd.num=self.num+other.num
          fadd.den=self.den
          return fadd
        else:
          fadd.den=self.den*other.den
          fadd.num=self.den*other.num + self.num*other.den
          return fadd
    def __sub__(self,other):
        fsub=Fraccion(0,0)
        if self.den==other.den:
          fsub.num=self.num-other.num
          fsub.den=self.den
          return fsub
        else:
          fsub.den=self.den*other.den
          fsub.num=- self.den*other.num + self.num*other.den
          return fsub
    def __mul__(self,other):
        r=Fraccion(0,0)
        r.num=self.num*other.num
        r.den=self.den*other.den
        return r
    def __truediv__(self,other):
        rdiv=Fraccion(0,0)
        rdiv.num=self.num*other.den
        rdiv.den=self.den*other.num
        return rdiv

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
         