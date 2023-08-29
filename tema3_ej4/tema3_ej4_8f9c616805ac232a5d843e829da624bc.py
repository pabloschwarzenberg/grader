class Fraccion:
    def __init__(self, numerador, denominador):
        self.num = numerador
        self.den = denominador

    def __add__(self, other):
        if self.den == other.den:
            return Fraccion(self.num + other.num, self.den)
        else:
            denominador_comun = self.den * other.den
            numerador1 = self.num * other.den
            numerador2 = other.num * self.den
            return Fraccion(numerador1 + numerador2, denominador_comun)

    def __sub__(self, other):
        if self.den == other.den:
            return Fraccion(self.num - other.num, self.den)
        else:
            denominador_comun = self.den * other.den
            numerador1 = self.num * other.den
            numerador2 = other.num * self.den
            return Fraccion(numerador1 - numerador2, denominador_comun)

    def __mul__(self, other):
        return Fraccion(self.num * other.num, self.den * other.den)

    def __truediv__(self, other):
        return Fraccion(self.num * other.den, self.den * other.num)

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


# Ejemplo de uso
if __name__ == "__main__":
    f = input("Ingresa la primera fracción [a/b]: ")
    f = f.split("/")
    f1 = Fraccion(int(f[0]), int(f[1]))
    f = input("Ingresa la segunda fracción [c/d]: ")
    f = f.split("/")
    f2 = Fraccion(int(f[0]), int(f[1]))
    print("La suma es ", f1 + f2)
    print("La resta es ", f1 - f2)
    print("La multiplicación es ", f1 * f2)
    print("La división es ", f1 / f2)

    