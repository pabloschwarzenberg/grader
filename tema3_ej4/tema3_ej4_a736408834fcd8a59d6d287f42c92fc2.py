class Fraccion:
    def __init__(self, numerador, denominador):
        self.num = numerador
        self.den = denominador

    def __add__(self, other):
        num_nuevo = self.num * other.den + other.num * self.den
        den_nuevo = self.den * other.den
        return Fraccion(num_nuevo, den_nuevo)

    def __sub__(self, other):
        num_nuevo = self.num * other.den - other.num * self.den
        den_nuevo = self.den * other.den
        return Fraccion(num_nuevo, den_nuevo)

    def __mul__(self, other):
        num_nuevo = self.num * other.num
        den_nuevo = self.den * other.den
        return Fraccion(num_nuevo, den_nuevo)

    def __truediv__(self, other):
        num_nuevo = self.num * other.den
        den_nuevo = self.den * other.num
        return Fraccion(num_nuevo, den_nuevo)

    def __repr__(self):
        entero = self.num // self.den
        if entero > 0:
            resto = self.num % self.den
            if resto > 0:
                return "{0} {1}/{2}".format(entero, resto, self.den)
            else:
                return "{0}".format(
