class Fraccion:
    def __init__(self, numerador, denominador):
        self.num = numerador
        self.den = denominador

    def __add__(self, other):
        num_resultado = self.num * other.den + self.den * other.num
        den_resultado = self.den * other.den
        return Fraccion(num_resultado, den_resultado)

    def __sub__(self, other):
        num_resultado = self.num * other.den - self.den * other.num
        den_resultado = self.den * other.den
        return Fraccion(num_resultado, den_resultado)

    def __mul__(self, other):
        num_resultado = self.num * other.num
        den_resultado = self.den * other.den
        return Fraccion(num_resultado, den_resultado)

    def __truediv__(self, other):
        num_resultado = self.num * other.den
        den_resultado = self.den * other.num
        return Fraccion(num_resultado, den_resultado)

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
    f = input("Ingresa la primera fracción [a/b]: ")
    f = f.split("/")
    f1 = Fraccion(int(f[0]), int(f[1]))

    f = input("Ingresa la segunda fracción [c/d]: ")
    f = f.split("/")
    f2 = Fraccion(int(f[0]), int(f[1]))

    suma = f1 + f2
    resta = f1 - f2
    multiplicacion = f1 * f2
    division = f1 / f2

    print("La suma es", suma)
    print("La resta es", resta)
    print("La multiplicación es", multiplicacion)
    print("La división es", division)

         