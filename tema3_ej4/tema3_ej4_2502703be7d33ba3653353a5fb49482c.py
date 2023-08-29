class Fraccion:
    def __init__(self, numerador, denominador):
        self.num = numerador
        self.den = denominador

    def __add__(self, other):
        if isinstance(other, Fraccion):
            denominador_comun = self.den * other.den
            numerador_resultado = (self.num * other.den) + (other.num * self.den)
            return Fraccion(numerador_resultado, denominador_comun)
        else:
            raise TypeError("No se puede sumar una Fraccion con otro tipo.")

    def __sub__(self, other):
        if isinstance(other, Fraccion):
            denominador_comun = self.den * other.den
            numerador_resultado = (self.num * other.den) - (other.num * self.den)
            return Fraccion(numerador_resultado, denominador_comun)
        else:
            raise TypeError("No se puede restar una Fraccion con otro tipo.")

    def __mul__(self, other):
        if isinstance(other, Fraccion):
            numerador_resultado = self.num * other.num
            denominador_resultado = self.den * other.den
            return Fraccion(numerador_resultado, denominador_resultado)
        else:
            raise TypeError("No se puede multiplicar una Fraccion con otro tipo.")

    def __truediv__(self, other):
        if isinstance(other, Fraccion):
            numerador_resultado = self.num * other.den
            denominador_resultado = self.den * other.num
            return Fraccion(numerador_resultado, denominador_resultado)
        else:
            raise TypeError("No se puede dividir una Fraccion con otro tipo.")

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
    f = input("Ingresa la primera fraccion [a/b]: ")
    f = f.split("/")
    f1 = Fraccion(int(f[0]), int(f[1]))

    f = input("Ingresa la segunda fraccion [c/d]: ")
    f = f.split("/")
    f2 = Fraccion(int(f[0]), int(f[1]))

    print("La suma es", f1 + f2)
    print("La resta es", f1 - f2)
    print("La multiplicación es", f1 * f2)
    print("La división es", f1 / f2)



         