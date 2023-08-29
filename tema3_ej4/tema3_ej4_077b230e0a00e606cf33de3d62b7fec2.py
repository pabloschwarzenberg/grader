class Fraccion:
    def __init__(self, numerador, denominador):
        self.num = numerador
        self.den = denominador

    def __add__(self, other):
        if isinstance(other, Fraccion):
            nuevo_denominador = self.den * other.den
            nuevo_numerador = (self.num * other.den) + (other.num * self.den)
            return Fraccion(nuevo_numerador, nuevo_denominador)
        else:
            raise TypeError("Operandos inválidos para la suma de fracciones.")

    def __sub__(self, other):
        if isinstance(other, Fraccion):
            nuevo_denominador = self.den * other.den
            nuevo_numerador = (self.num * other.den) - (other.num * self.den)
            return Fraccion(nuevo_numerador, nuevo_denominador)
        else:
            raise TypeError("Operandos inválidos para la resta de fracciones.")

    def __mul__(self, other):
        if isinstance(other, Fraccion):
            nuevo_numerador = self.num * other.num
            nuevo_denominador = self.den * other.den
            return Fraccion(nuevo_numerador, nuevo_denominador)
        else:
            raise TypeError("Operandos inválidos para la multiplicación de fracciones.")

    def __truediv__(self, other):
        if isinstance(other, Fraccion):
            nuevo_numerador = self.num * other.den
            nuevo_denominador = self.den * other.num
            return Fraccion(nuevo_numerador, nuevo_denominador)
        else:
            raise TypeError("Operandos inválidos para la división de fracciones.")

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
