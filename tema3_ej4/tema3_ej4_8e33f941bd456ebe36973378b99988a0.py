class Fraccion:
    def __init__(self, numerador, denominador):
        self.num = numerador
        self.den = denominador

    def __add__(self, other):
        if isinstance(other, Fraccion):
            num_sum = self.num * other.den + other.num * self.den
            den_sum = self.den * other.den
            return Fraccion(num_sum, den_sum)
        else:
            raise TypeError("La suma solo es válida entre dos objetos de la clase Fraccion")

    def __sub__(self, other):
        if isinstance(other, Fraccion):
            num_sub = self.num * other.den - other.num * self.den
            den_sub = self.den * other.den
            return Fraccion(num_sub, den_sub)
        else:
            raise TypeError("La resta solo es válida entre dos objetos de la clase Fraccion")

    def __mul__(self, other):
        if isinstance(other, Fraccion):
            num_mul = self.num * other.num
            den_mul = self.den * other.den
            return Fraccion(num_mul, den_mul)
        else:
            raise TypeError("La multiplicación solo es válida entre dos objetos de la clase Fraccion")

    def __truediv__(self, other):
        if isinstance(other, Fraccion):
            num_div = self.num * other.den
            den_div = self.den * other.num
            return Fraccion(num_div, den_div)
        else:
            raise TypeError("La división solo es válida entre dos objetos de la clase Fraccion")

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