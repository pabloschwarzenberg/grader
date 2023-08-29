class Fraccion:
    def __init__(self, numerador, denominador):
        self.num = numerador
        self.den = denominador

    def __add__(self, other):
        if isinstance(other, Fraccion):
            num = self.num * other.den + other.num * self.den
            den = self.den * other.den
            return Fraccion(num, den)
        else:
            raise TypeError("El objeto pasado como parámetro no es de la clase Fraccion")

    def __sub__(self, other):
        if isinstance(other, Fraccion):
            num = self.num * other.den - other.num * self.den
            den = self.den * other.den
            return Fraccion(num, den)
        else:
            raise TypeError("El objeto pasado como parámetro no es de la clase Fraccion")

    def __truediv__(self, other):
        if isinstance(other, Fraccion):
            num = self.num * other.den
            den = self.den * other.num
            return Fraccion(num, den)
        else:
            raise TypeError("El objeto pasado como parámetro no es de la clase Fraccion")

    def __mul__(self, other):
        if isinstance(other, Fraccion):
            num = self.num * other.num
            den = self.den * other.den
            return Fraccion(num, den)
        else:
            raise TypeError("El objeto pasado como parámetro no es de la clase Fraccion")

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
