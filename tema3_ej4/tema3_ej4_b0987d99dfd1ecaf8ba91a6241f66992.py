class Fraccion:
    def __init__(self, numerador, denominador):
        self.num = numerador
        self.den = denominador

    def __add__(self, other):
        if isinstance(other, Fraccion):
            denominador_comun = self.den * other.den
            numerador_suma = (self.num * other.den) + (other.num * self.den)
            return Fraccion(numerador_suma, denominador_comun)
        else:
            raise TypeError("Operación inválida,se necesita una Fraccion para la multiplicación")

    def __sub__(self, other):
        if isinstance(other, Fraccion):
            denominador_comun = self.den * other.den
            numerador_resta = (self.num * other.den) - (other.num * self.den)
            return Fraccion(numerador_resta, denominador_comun)
        else:
            raise TypeError("Operación inválida, se necesita una Fraccion para la multiplicación")

    def __mul__(self, other):
        if isinstance(other, Fraccion):
            numerador_mul = self.num * other.num
            denominador_mul = self.den * other.den
            return Fraccion(numerador_mul, denominador_mul)
        else:
            raise TypeError("Operación inválida, se necesita una Fraccion para la multiplicación")

    def __truediv__(self, other):
        if isinstance(other, Fraccion):
            numerador_div = self.num * other.den
            denominador_div = self.den * other.num
            return Fraccion(numerador_div, denominador_div)
        else:
            raise TypeError("Operación inválida, se necesita una Fraccion para la multiplicación")

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