class Fraccion:
    def __init__(self,numerador,denominador):
        self.numerador=numerador
        self.denominador=denominador
    def __add__(self,f):
        n=(self.numerador*f.denominador+self.denominador*f.numerador)
        d=(self.denominador*f.denominador)
        resultante=Fraccion(n,d)
        return resultante
    def __sub__(self,f):
        n=(self.numerador*f.denominador-f.numerador*self.denominador)
        d=(self.denominador*f.denominador)
        resultado=Fraccion(n,d)
        return resultado
    def __mul__(self,f):
        n=(self.numerador*f.numerador)
        d=(self.denominador*f.denominador)
        resultado=Fraccion(n,d)
        return  resultado
    def __truediv__(self,f):
        n=self.numerador*f.denominador
        d=self.denominador*f.numerador
        resultado=Fraccion(n,d)
        return resultado
    def __repr__(self):
        entero=self.numerador//self.denominador
        if entero>0:
            resto=self.numerador%self.denominador
            if resto>0:
                return "{0} {1}/{2}".format(entero,resto,self.denominador)
            else:
                return "{0}".format(entero)
        else:
            return "{0}/{1}".format(self.numerador,self.denominador)

    def a_numero(self):
        return self.numerador/self.denominador

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
         