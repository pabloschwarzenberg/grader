class Fraccion:
    def __init__(self, numerador, denominador):
        self.num = numerador
        self.den = denominador

    def __add__(self, other):
        if isinstance(other, Fraccion):
            numerador_suma = self.num * other.den + other.num * self.den
            denominador_suma = self.den * other.den
            return Fraccion(numerador_suma, denominador_suma)
        else:
            raise TypeError("Tipo de operando no soportado.")

    def __sub__(self, other):
        if isinstance(other, Fraccion):
            numerador_resta = self.num * other.den - other.num * self.den
            denominador_resta = self.den * other.den
            return Fraccion(numerador_resta, denominador_resta)
        else:
            raise TypeError("Tipo de operando no soportado.")

    def __mul__(self, other):
        if isinstance(other, Fraccion):
            numerador_mul = self.num * other.num
            denominador_mul = self.den * other.den
            return Fraccion(numerador_mul, denominador_mul)
        else:
            raise TypeError("Tipo de operando no soportado.")

    def __truediv__(self, other):
        if isinstance(other, Fraccion):
            numerador_div = self.num * other.den
            denominador_div = self.den * other.num
            return Fraccion(numerador_div, denominador_div)
        else:
            raise TypeError("Tipo de operando no soportado.")

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

if __name__ == "__main__":
    f = input("Ingresa la primera fracción [a/b]: ")
    f = f.split("/")
    f1 = Fraccion(int(f[0]), int(f[1]))
    f = input("Ingresa la segunda fracción [c/d]: ")
    f = f.split("/")
    f2 = Fraccion(int(f[0]), int(f[1]))
    print("La suma es", f1 + f2)
    print("La resta es", f1 - f2)
    print("La multiplicación es", f1 * f2)
    print("La división es", f1 / f2)
