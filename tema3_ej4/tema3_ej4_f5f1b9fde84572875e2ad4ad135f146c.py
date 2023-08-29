class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def __str__(self):
        return "{}/{}".format(self.numerador, self.denominador)

    def simplificar(self):
        divisor = self.mcd(self.numerador, self.denominador)
        self.numerador //= divisor
        self.denominador //= divisor

    def mcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def __add__(self, other):
        nuevo_numerador = (self.numerador * other.denominador) + (self.denominador * other.numerador)
        nuevo_denominador = self.denominador * other.denominador
        resultado = Fraccion(nuevo_numerador, nuevo_denominador)
        resultado.simplificar()
        return resultado

    def __sub__(self, other):
        nuevo_numerador = (self.numerador * other.denominador) - (self.denominador * other.numerador)
        nuevo_denominador = self.denominador * other.denominador
        resultado = Fraccion(nuevo_numerador, nuevo_denominador)
        resultado.simplificar()
        return resultado

    def __mul__(self, other):
        nuevo_numerador = self.numerador * other.numerador
        nuevo_denominador = self.denominador * other.denominador
        resultado = Fraccion(nuevo_numerador, nuevo_denominador)
        resultado.simplificar()
        return resultado

    def __truediv__(self, other):
        nuevo_numerador = self.numerador * other.denominador
        nuevo_denominador = self.denominador * other.numerador
        resultado = Fraccion(nuevo_numerador, nuevo_denominador)
        resultado.simplificar()
        return resultado

if __name__ == "__main__":
    re1=Fraccion(4,5)
    ro1=Fraccion(1,2)
    re2=Fraccion(3,4)
    re3=re1+ro1
    print(re1, "+", ro1, "=", re3)
    if re1.numerador/re1.denominador == re1:
        print("multiplicacion correcta")
    if re1.numerador/re1.denominador != ro1:
        print("multiplicacion incorrecta")
    ro3=re1*re2
    print(ro3)
    if re1.numerador*re2.numerador/re1.denominador/re2.denominador == ro3:
        print("multiplicacion correcta")
    if re1.numerador*re2.numerador/re1.denominador/re2.denominador != ro3:
        print("multiplicacion incorrecta")
    re4=re1-re2
    print(re4)
    if re1.numerador/re1.denominador-re2.numerador/re2.denominador == re4:
        print("resta correcta")
    if re1.numerador/re1.denominador-re2.numerador/re2.denominador != re4:
        print("resta incorrecta")
    if re1.numerador/re1.denominador != re4:
        print("resta incorrecta")
    if re1.numerador/re1.den



