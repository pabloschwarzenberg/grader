class Fraccion:
    def __init__(self, numerador, denominador):
        self.num = numerador
        self.den = denominador

    def __add__(self, other):
        if isinstance(other, Fraccion):
            # Calcula el numerador y denominador de la fracción resultante
            numerador = self.num * other.den + other.num * self.den
            denominador = self.den * other.den
            return Fraccion(numerador, denominador)
        else:
            raise TypeError("El otro objeto no es una Fraccion")

    def __sub__(self, other):
        if isinstance(other, Fraccion):
            # Calcula el numerador y denominador de la fracción resultante
            numerador = self.num * other.den - other.num * self.den
            denominador = self.den * other.den
            return Fraccion(numerador, denominador)
        else:
            raise TypeError("El otro objeto no es una Fraccion")

    def __mul__(self, other):
        if isinstance(other, Fraccion):
            # Calcula el numerador y denominador de la fracción resultante
            numerador = self.num * other.num
            denominador = self.den * other.den
            return Fraccion(numerador, denominador)
        else:
            raise TypeError("El otro objeto no es una Fraccion")

    def __truediv__(self, other):
        if isinstance(other, Fraccion):
            # Calcula el numerador y denominador de la fracción resultante
            numerador = self.num * other.den
            denominador = self.den * other.num
            return Fraccion(numerador, denominador)
        else:
            raise TypeError("El otro objeto no es una Fraccion")

    def __repr__(self):
        entero = self.num // self.den
        resto = self.num % self.den

        if entero > 0:
            if resto > 0:
                return "{0} {1}/{2}".format(entero, resto, self.den)
            else:
                return "{0}".format(entero)
        else:
            return "{0}/{1}".format(self.num, self.den)

    def a_numero(self):
        return self.num / self.den


if __name__ == "__main__":
    f1 = Fraccion(1, 2)
    f2 = Fraccion(3, 4)

    suma = f1 + f2
    resta = f1 - f2
    multiplicacion = f1 * f2
    division = f1 / f2

    print("La suma es", suma)
    print("La resta es", resta)
    print("La multiplicación es", multiplicacion)
    print("La división es", division)
