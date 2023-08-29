class Fraccion:
    def __init__(self,numerador,denominador):
        self.num=numerador
        self.den=denominador
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
            raise TypeError("Operación no válida. Se requiere un objeto de tipo Fraccion.")

    def __sub__(self, other):
        if isinstance(other, Fraccion):
            nuevo_denominador = self.den * other.den
            nuevo_numerador = (self.num * other.den) - (other.num * self.den)
            return Fraccion(nuevo_numerador, nuevo_denominador)
        else:
            raise TypeError("Operación no válida. Se requiere un objeto de tipo Fraccion.")

    def __mul__(self, other):
        if isinstance(other, Fraccion):
            nuevo_numerador = self.num * other.num
            nuevo_denominador = self.den * other.den
            return Fraccion(nuevo_numerador, nuevo_denominador)
        else:
            raise TypeError("Operación no válida. Se requiere un objeto de tipo Fraccion.")

    def __truediv__(self, other):
        if isinstance(other, Fraccion):
            nuevo_numerador = self.num * other.den
            nuevo_denominador = self.den * other.num
            return Fraccion(nuevo_numerador, nuevo_denominador)
        else:
            raise TypeError("Operación no válida. Se requiere un objeto de tipo Fraccion.")

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

    print("La suma es ", f1 + f2)
    print("La resta es ", f1 - f2)
    print("La multiplicación es ", f1 * f2)
    print("La división es ", f1 / f2)
