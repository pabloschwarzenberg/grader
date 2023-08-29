class Fraccion:
    def __init__(self,numerador=0,denominador=0):
        self.numerador=numerador
        self.denominador=denominador

    def __mul__(self,other):
        r=Fraccion(0,0)
        r.numerador=self.numerador*other.numerador
        r.denominador=self.denominador*other.denominador
        return r
    def __add__(self,other):
        final=Fraccion(0,0)
        final.numerador=self.numerador*other.denominador+self.denominador*other.numerador
        final.denominador=self.denominador*other.denominador
        return final
    def __div__(self,other):
        r=Fraccion(0,0)
        r.numerador=self.numerador*other.denominador
        r.denominador=self.denominador*other.numerador
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
         