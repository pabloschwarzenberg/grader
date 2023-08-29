class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador
    
    def simplificar(self):
        # Calcula el maximo comun divisor entre el numerador y el denominador
        mcd = self.mcd(self.numerador, self.denominador)
        
        # Simplifica la fraccion dividiendo ambos terminos por el mcd
        self.numerador //= mcd
        self.denominador //= mcd
    
    def mcd(self, a, b):
        # Calcula el maximo comun divisor utilizando el algoritmo de Euclides
        while b != 0:
            a, b = b, a % b
        return a
    
    def __add__(self, other):
        if isinstance(other, Fraccion):
            # Calcula la suma de dos fracciones
            nuevo_numerador = self.numerador * other.denominador + other.numerador * self.denominador
            nuevo_denominador = self.denominador * other.denominador
            suma = Fraccion(nuevo_numerador, nuevo_denominador)
            suma.simplificar()
            return suma
        else:
            raise TypeError("El objeto debe ser de tipo Fraccion")
    
    def __sub__(self, other):
        if isinstance(other, Fraccion):
            # Calcula la resta de dos fracciones
            nuevo_numerador = self.numerador * other.denominador - other.numerador * self.denominador
            nuevo_denominador = self.denominador * other.denominador
            resta = Fraccion(nuevo_numerador, nuevo_denominador)
            resta.simplificar()
            return resta
        else:
            raise TypeError("El objeto debe ser de tipo Fraccion")
    
    def __truediv__(self, other):
        if isinstance(other, Fraccion):
            # Calcula la division de dos fracciones
            nuevo_numerador = self.numerador * other.denominador
            nuevo_denominador = self.denominador * other.numerador
            division = Fraccion(nuevo_numerador, nuevo_denominador)
            division.simplificar()
            return division
        else:
            raise TypeError("El objeto debe ser de tipo Fraccion")

# Ejemplo de uso
fraccion1 = Fraccion(1, 2)
fraccion2 = Fraccion(3, 4)

# Suma de fracciones
suma = fraccion1 + fraccion2
print("Suma:", suma.numerador, "/", suma.denominador)

# Resta de fracciones
resta = fraccion1 - fraccion2
print("Resta:", resta.numerador, "/", resta.denominador)

# Division de fracciones
division = fraccion1 / fraccion2
print("Division:", division.numerador, "/", division.denominador)
