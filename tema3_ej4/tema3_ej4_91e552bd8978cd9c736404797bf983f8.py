class Fracción:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def simplificar(self):
        # Calcular el máximo común divisor
        mcd = self.calcular_mcd(self.numerador, self.denominador)

        # Simplificar la fracción dividiendo el numerador y el denominador por el mcd
        self.numerador //= mcd
        self.denominador //= mcd

    @staticmethod
    def calcular_mcd(a, b):
        # Calcular el máximo común divisor utilizando el algoritmo de Euclides
        while b != 0:
            a, b = b, a % b
        return a

    def __add__(self, other):
        if isinstance(other, Fracción):
            denominador_comun = self.denominador * other.denominador
            numerador_suma = (self.numerador * other.denominador) + (other.numerador * self.denominador)
            return Fracción(numerador_suma, denominador_comun)
        else:
            raise TypeError("Operación no válida. Se requiere un objeto de tipo Fracción.")

    def __sub__(self, other):
        if isinstance(other, Fracción):
            denominador_comun = self.denominador * other.denominador
            numerador_resta = (self.numerador * other.denominador) - (other.numerador * self.denominador)
            return Fracción(numerador_resta, denominador_comun)
        else:
            raise TypeError("Operación no válida. Se requiere un objeto de tipo Fracción.")

    def __truediv__(self, other):
        if isinstance(other, Fracción):
            numerador_división = self.numerador * other.denominador
            denominador_división = self.denominador * other.numerador
            return Fracción(numerador_división, denominador_división)
        else:
            raise TypeError("Operación no válida. Se requiere un objeto de tipo Fracción.")

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"
