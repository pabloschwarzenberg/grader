from fractions import Fraction

class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def __add__(self, other):
        return Fraccion(self.numerador * other.denominador + other.numerador * self.denominador,
                        self.denominador * other.denominador)

    def __sub__(self, other):
        return Fraccion(self.numerador * other.denominador - other.numerador * self.denominador,
                        self.denominador * other.denominador)

    def __truediv__(self, other):
        return Fraccion(self.numerador * other.denominador,
                        self.denominador * other.numerador)