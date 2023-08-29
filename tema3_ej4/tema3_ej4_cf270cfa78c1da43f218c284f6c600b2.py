class Fraccion:
    def __init__(self, numerador, denominador):
        self.num = numerador
        self.den = denominador

    def __add__(self, other):
        resultado_num = self.num * other.den + other.num * self.den
        resultado_den = self.den * other.den
        return Fraccion(resultado_num, resultado_den)

    def __sub__(self, other):
        resultado_num = self.num * other.den - other.num * self.den
        resultado_den = self.den * other.den
        return Fraccion(resultado_num, resultado_den)

    def __mul__(self, other):
        resultado_num = self.num * other.num
        resultado_den = self.den * other.den
        return Fraccion(resultado_num, resultado_den)

    def __truediv__(self, other):
        resultado_num = self.num * other.den
        resultado_den = self.den * other.num
        return Fraccion(resultado_num, resultado_den)

    def __repr__(self):
        entero = self.num // self.den
        resto = self.num % self.den

        if entero > 0:
            if resto > 0:
                return f"{entero} {resto}/{self.den}"
            else:
                return f"{entero}"
        else:
            return f"{self.num}/{self.den}"

    def a_numero(self):
        return self.num / self.den