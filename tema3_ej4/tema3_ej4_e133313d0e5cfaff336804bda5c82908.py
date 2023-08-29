class Fraccion:
    def _init_(self,numerador,denominador):
        self.numerador = numerador
        self.denominador = denominador

    def _mul_(self,other):
        r = Fraccion(0,0)
        r.numerador = self.numerador*other.numerador
        r.denominador = self.denominador*other.denominador
        return r
    
    def _add_(self, otro):
        return Fraccion(self.numerador * otro.denominador + self.denominador * otro.numerador,self.denonimador * otro.denominador)
    
    def _sub_(self,other):
        res = Fraccion(0,0)
        res.numerador = self.numerador*other.denominador - other.numerador*self.denominador
        res.denominador = self.denominador*other.denominador
        return res
        
    def _truediv_(self,other):
        div = Fraccion(0,0)
        div.numerador = self.numerador*other.denominador
        div.denominador = self.denominador*other.numerador
        return div
        
    def _repr_(self):
        entero = self.numerador//self.denominador
        if entero > 0:
            resto = self.numerador%self.denominador
            if resto > 0:
                return "{0} {1}/{2}".format(entero,resto,self.denominador)
            else:
                return "{0}".format(entero)
        else:
            return "{0}/{1}".format(self.numerador,self.denominador)

    def a_numero(self):
        return self.numerador/self.denominador

if __name__ == "_main_":
    f = input("Ingresa la primera fraccion [a/b]: ")
    f = f.split("/")
    f1 = Fraccion(int(f[0]),int(f[1]))
    f = input("Ingresa la segunda fraccion [c/d]: ")
    f = f.split("/")
    f2 = Fraccion(int(f[0]),int(f[1]))
    print("La suma es ",f1+f2)
    print("La resta es ",f1-f2)
    print("La multiplicación es ",f1*f2)
    print("La división es ",f1/f2)
         