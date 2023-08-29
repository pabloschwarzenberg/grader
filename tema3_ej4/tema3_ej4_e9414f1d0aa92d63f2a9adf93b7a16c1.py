class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def simplificar(self):
        # Calcula el máximo común divisor (MCD) usando el algoritmo de Euclides
        a = self.numerador
        b = self.denominador
        while b != 0:
            a, b = b, a % b
        mcd = a

        # Simplifica la fracción dividiendo el numerador y denominador por el MCD
        self.numerador //= mcd
        self.denominador //= mcd

    def __add__(self, other):
        # Suma de fracciones: (a/b) + (c/d) = (ad + bc) / (bd)
        numerador = self.numerador * other.denominador + self.denominador * other.numerador
        denominador = self.denominador * other.denominador
        resultado = Fraccion(numerador, denominador)
        resultado.simplificar()
        return resultado

    def __sub__(self, other):
        # Resta de fracciones: (a/b) - (c/d) = (ad - bc) / (bd)
        numerador = self.numerador * other.denominador - self.denominador * other.numerador
        denominador = self.denominador * other.denominador
        resultado = Fraccion(numerador, denominador)
        resultado.simplificar()
        return resultado

    def __truediv__(self, other):
        # División de fracciones: (a/b) / (c/d) = (a*d) / (b*c)
        numerador = self.numerador * other.denominador
        denominador = self.denominador * other.numerador
        resultado = Fraccion(numerador, denominador)
        resultado.simplificar()
        return resultado

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"


if __name__ == "__main__":
    f1 = Fraccion(1, 2)
    f2 = Fraccion(3, 4)

    f3 = f1 + f2
    print(f3)  # 5/4

    f4 = f1 - f2
    print(f4)  # -1/4

    f5 = f1 / f2
    print(f5)  # 2/3
