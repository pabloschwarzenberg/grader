class Fraccion:
    def __init__(self, numerador, denominador):
        # Validar que el numerador y el denominador sean enteros
        if isinstance(numerador, int) and isinstance(denominador, int):
            # Validar que el denominador no sea cero
            if denominador != 0:
                # Simplificar la fracción si es posible
                self.numerador = numerador // self.mcd(numerador, denominador)
                self.denominador = denominador // self.mcd(numerador, denominador)
            else:
                raise ZeroDivisionError("El denominador no puede ser cero")
        else:
            raise TypeError("El numerador y el denominador deben ser enteros")
    
    def mcd(self, a, b):
        # Calcular el máximo común divisor de dos números usando el algoritmo de Euclides
        while b != 0:
            a, b = b, a % b
        return a
    
    def __str__(self):
        return f"{self.numerador}/{self.denominador}"
    
    def __add__(self, other):
        # Sumar dos fracciones usando el mínimo común múltiplo de los denominadores
        if isinstance(other, Fraccion):
            mcm = (self.denominador * other.denominador) // self.mcd(self.denominador, other.denominador)
            return Fraccion((self.numerador * (mcm // self.denominador)) + (other.numerador * (mcm // other.denominador)), mcm)
        else:
            raise TypeError("Solo se pueden sumar fracciones con fracciones")
    
    def __sub__(self, other):
        # Restar dos fracciones usando el mínimo común múltiplo de los denominadores
        if isinstance(other, Fraccion):
            mcm = (self.denominador * other.denominador) // self.mcd(self.denominador, other.denominador)
            return Fraccion((self.numerador * (mcm // self.denominador)) - (other.numerador * (mcm // other.denominador)), mcm)
        else:
            raise TypeError("Solo se pueden restar fracciones con fracciones")
    
    def __truediv__(self, other):
        # Dividir dos fracciones invirtiendo y multiplicando la segunda fracción
        if isinstance(other, Fraccion):
            return Fraccion(self.numerador * other.denominador, self.denominador * other.numerador)
        else:
            raise TypeError("Solo se pueden dividir fracciones con fracciones")
