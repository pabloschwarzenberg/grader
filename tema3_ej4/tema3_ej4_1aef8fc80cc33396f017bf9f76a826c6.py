class Fracción:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def simplificar(self):
        mcd = self.calcular_mcd(self.numerador, self.denominador)
        self.numerador //= mcd
        self.denominador //= mcd

    @staticmethod
    def calcular_mcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def __add__(self, other):
        nuevo_numerador = self.numerador * other.denominador + other.numerador * self.denominador
        nuevo_denominador = self.denominador * other.denominador
        resultado = Fracción(nuevo_numerador, nuevo_denominador)
        resultado.simplificar()
        return resultado

    def __sub__(self, other):
        nuevo_numerador = self.numerador * other.denominador - other.numerador * self.denominador
        nuevo_denominador = self.denominador * other.denominador
        resultado = Fracción(nuevo_numerador, nuevo_denominador)
        resultado.simplificar()
        return resultado

    def __truediv__(self, other):
        nuevo_numerador = self.numerador * other.denominador
        nuevo_denominador = self.denominador * other.numerador
        resultado = Fracción(nuevo_numerador, nuevo_denominador)
        resultado.simplificar()
        return resultado

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"

if __name__ == "__main__":
    fraccion1 = Fracción(3, 4)
    fraccion2 = Fracción(2, 5)

    suma = fraccion1 + fraccion2
    print("Suma:", suma)

    resta = fraccion1 - fraccion2
    print("Resta:", resta)

    division = fraccion1 / fraccion2
    print("División:", division)

         