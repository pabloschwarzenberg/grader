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
                return "{0} {1}/{2}".format(entero,resto,self.denominador)
            else:
                return "{0}".format(entero)
        else:
            return "{0}/{1}".format(self.numerador,self.denominador)

    def a_numero(self):
        return self.numerador/self.denominador

    def __add__(self,other):
        s = Fraccion(0,0)
        if self.denominador == other.denominador:
            s.numerador = self.numerador + other.numerador
            s.denominador = self.denominador
            return s
        else:
            s.denominador = self.denominador * other.denominador
            s.numerador = self.numerador * other.denominador + other.numerador * self.denominador
            return s
            
    def __sub__(self,other):
        s = Fraccion(0,0)
        if self.denominador == other.denominador:
            s.numerador = self.numerador - other.numerador
            s.denominador = self.denominador
            return s
        else:
            s.denominador = self.denominador * other.denominador
            s.numerador = self.numerador * other.denominador - other.numerador * self.denominador
            return s
    def __truediv__(self,other):
        s = Fraccion(0,0)
        divisor = Fraccion(other.denominador,other.numerador)
        s.numerador = self.numerador*divisor.numerador
        s.denominador = self.denominador*divisor.denominador
        return s


         