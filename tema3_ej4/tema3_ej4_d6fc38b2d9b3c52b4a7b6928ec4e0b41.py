class Fraccion:
    def __init__(self, numerador, denominador):
        self.num = numerador
        self.den = denominador

    def __add__(self, other):
        numerador = self.num * other.den + other.num * self.den
        denominador = self.den * other.den
        return Fraccion(numerador, denominador)

    def __sub__(self, other):
        numerador = self.num * other.den - other.num * self.den
        denominador = self.den * other.den
        return Fraccion(numerador, denominador)

    def __mul__(self, other):
        numerador = self.num * other.num
        denominador = self.den * other.den
        return Fraccion(numerador, denominador)

    def __truediv__(self, other):
        numerador = self.num * other.den
        denominador = self.den * other.num
        return Fraccion(numerador, denominador)

    def __repr__(self):
        entero = self.num // self.den
        if entero > 0:
            resto = self.num % self.den
            if resto > 0:
                return "{0} {1}/{2}".format(entero, resto, self.den)
            else:
                return "{0}".format(entero)
        else:
            return "{0}/{1}".format(self.num, self.den)

    def a_numero(self):
        return self.num / self.den

         