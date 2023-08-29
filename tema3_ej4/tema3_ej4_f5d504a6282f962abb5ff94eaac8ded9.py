class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def simplificar(self):
        # Calcula el máximo común divisor (MCD) entre el numerador y el denominador
        mcd = self.calcular_mcd(self.numerador, self.denominador)

        # Simplifica la fracción dividiendo el numerador y el denominador por el MCD
        self.numerador //= mcd
        self.denominador //= mcd

    def calcular_mcd(self, a, b):
        # Calcula el máximo común divisor utilizando el algoritmo de Euclides
        while b != 0:
            a, b = b, a % b
        return a

    def __add__(self, other):
        if isinstance(other, Fraccion):
            # Calcula el denominador común
            denominador_comun = self.denominador * other.denominador

            # Calcula los nuevos numeradores
            numerador_1 = self.numerador * other.denominador
            numerador_2 = other.numerador * self.denominador

            # Calcula el numerador de la fracción resultante
            numerador_resultante = numerador_1 + numerador_2

            # Crea y devuelve una nueva instancia de Fracción con la suma
            resultado = Fraccion(numerador_resultante, denominador_comun)
            resultado.simplificar()
            return resultado
        else:
            raise TypeError("Operands must be of type Fraccion")

    def __sub__(self, other):
        if isinstance(other, Fraccion):
            # Calcula el denominador común
            denominador_comun = self.denominador * other.denominador

            # Calcula los nuevos numeradores
            numerador_1 = self.numerador * other.denominador
            numerador_2 = other.numerador * self.denominador

            # Calcula el numerador de la fracción resultante
            numerador_resultante = numerador_1 - numerador_2

            # Crea y devuelve una nueva instancia de Fracción con la resta
            resultado = Fraccion(numerador_resultante, denominador_comun)
            resultado.simplificar()
            return resultado
        else:
            raise TypeError("Operands must be of type Fraccion")

    def __truediv__(self, other):
        if isinstance(other, Fraccion):
            # Invierte la segunda fracción y la multiplica por la primera
            numerador_resultante = self.numerador * other.denominador
            denominador_resultante = self.denominador * other.numerador

            # Crea y devuelve una nueva instancia de Fracción con la división
            resultado = Fraccion(numerador_resultante, denominador_resultante)
            resultado.simplificar()
            return resultado
        else:
            raise TypeError("Operands must be of type Fraccion")
