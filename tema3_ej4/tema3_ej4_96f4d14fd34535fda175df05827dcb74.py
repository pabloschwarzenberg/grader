class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def simplificar(self):
        gcd = self.calcular_mcd(self.numerador, self.denominador)
        self.numerador //= gcd
        self.denominador //= gcd

    def calcular_mcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def __add__(self, other):
        if isinstance(other, Fraccion):
            numerador = (self.numerador * other.denominador) + (other.numerador * self.denominador)
            denominador = self.denominador * other.denominador
            resultado = Fraccion(numerador, denominador)
            resultado.simplificar()
            return resultado
        else:
            raise TypeError("Unsupported operand type for +")

    def __sub__(self, other):
        if isinstance(other, Fraccion):
            numerador = (self.numerador * other.denominador) - (other.numerador * self.denominador)
            denominador = self.denominador * other.denominador
            resultado = Fraccion(numerador, denominador)
            resultado.simplificar()
            return resultado
        else:
            raise TypeError("Unsupported operand type for -")

    def __truediv__(self, other):
        if isinstance(other, Fraccion):
            numerador = self.numerador * other.denominador
            denominador = self.denominador * other.numerador
            resultado = Fraccion(numerador, denominador)
            resultado.simplificar()
            return resultado
        else:
            raise TypeError("Unsupported operand type for /")

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"

# Ejemplo de uso
f1 = Fraccion(1, 2)
f2 = Fraccion(3, 4)

f3 = f1 + f2
print(str(f3))  # Imprime: 5/4

f4 = f1 - f2
print(str(f4))  # Imprime: -1/4

f5 = f1 / f2
print(str(f5))  # Imprime: 2/3
