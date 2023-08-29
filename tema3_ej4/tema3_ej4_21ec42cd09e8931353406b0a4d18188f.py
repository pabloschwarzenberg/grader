class Fraccion:
    def __init__(self,numerador,denominador):
        self.numerador=numerador
        self.denominador=denominador

    def __mul__(self,other):
        r=Fraccion(0,0)
        r.numerador=self.numerador*other.numerador
        r.denominador=self.denominador*other.denominador
        return r

    def __repr__(self):
        entero=self.numerador//self.denominador
        if entero>0:
            resto=self.numerador%self.denominador
            if resto>0:
                return "{0} {1}/{2}".format(entero,resto,self.den)
            else:
                return "{0}".format(entero)
        else:
            return "{0}/{1}".format(self.numerador,self.denominador)

    def a_numero(self):
        return self.numerador/self.denominador

    def __add__(self, other):
        s=Fraccion(0,0)
        s.numerador=(self.numerador*other.denominador)+(other.numerador*self.denominador)
        s.denominador=self.denominador*other.denominador
        return s
    def __sub__(self, other):
        s=Fraccion(0,0)
        s.numerador=(self.numerador*other.denominador)-(other.numerador*self.denominador)
        s.denominador=self.denominador*other.denominador
        return s
    def __truediv__(self, other):
        s=Fraccion(0,0)
        s.numerador=self.numerador*other.denominador
        s.denominador=self.denominador*other.numerador
        return s
if __name__ == "__main__":
    f=input("Ingresa la primera frawordccion [a/b]: ")
    f=f.split("/")
    f1=Fraccion(int(f[0]),int(f[1]))
    f=input("Ingresa la segunda fraccion [c/d]: ")
    f=f.split("/")
    f2=Fraccion(int(f[0]),int(f[1]))
    print("La suma es ",f1+f2)
    print("La resta es ",f1-f2)
    print("La multiplicación es ",f1*f2)
    print("La división es ",f1/f2)
