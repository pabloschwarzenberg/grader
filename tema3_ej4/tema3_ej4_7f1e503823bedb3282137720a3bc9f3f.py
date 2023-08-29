class Fracción:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"

    def simplificar(self):
        mcd = self.calcular_mcd(self.numerador, self.denominador)
        self.numerador //= mcd
        self.denominador //= mcd

    def calcular_mcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def __add__(self, other):
        if isinstance(other, Fracción):
            denominador_comun = self.denominador * other.denominador
            numerador_1 = self.numerador * other.denominador
            numerador_2 = other.numerador * self.denominador
            numerador_total = numerador_1 + numerador_2
            return Fracción(numerador_total, denominador_comun)
        else:
            raise TypeError("Operación no válida. Debe sumar dos objetos de la clase Fracción.")

    def __sub__(self, other):
        if isinstance(other, Fracción):
            denominador_comun = self.denominador * other.denominador
            numerador_1 = self.numerador * other.denominador
            numerador_2 = other.numerador * self.denominador
            numerador_total = numerador_1 - numerador_2
            return Fracción(numerador_total, denominador_comun)
        else:
            raise TypeError("Operación no válida. Debe restar dos objetos de la clase Fracción.")

    def __truediv__(self, other):
        if isinstance(other, Fracción):
            numerador_total = self.numerador * other.denominador
            denominador_total = self.denominador * other.numerador
            return Fracción(numerador_total, denominador_total)
        else:
            raise TypeError("Operación no válida. Debe dividir dos objetos de la clase Fracción.")

         