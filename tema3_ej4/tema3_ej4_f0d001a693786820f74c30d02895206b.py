class Fracción:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador
    
    def __str__(self):
        return f"{self.numerador}/{self.denominador}"
    
    def __add__(self, otro):
        if isinstance(otro, Fracción):
            nuevo_numerador = (self.numerador * otro.denominador) + (otro.numerador * self.denominador)
            nuevo_denominador = self.denominador * otro.denominador
            return Fracción(nuevo_numerador, nuevo_denominador)
        else:
            raise TypeError("Tipo de operando no admitido. El operando debe ser una Fracción.")
    
    def __sub__(self, otro):
        if isinstance(otro, Fracción):
            nuevo_numerador = (self.numerador * otro.denominador) - (otro.numerador * self.denominador)
            nuevo_denominador = self.denominador * otro.denominador
            return Fracción(nuevo_numerador, nuevo_denominador)
        else:
            raise TypeError("Tipo de operando no admitido. El operando debe ser una Fracción.")
    
    def __truediv__(self, otro):
        if isinstance(otro, Fracción):
            nuevo_numerador = self.numerador * otro.denominador
            nuevo_denominador = self.denominador * otro.numerador
            return Fracción(nuevo_numerador, nuevo_denominador)
        else:
            raise TypeError("Tipo de operando no admitido. El operando debe ser una Fracción.")

# Ejemplo de uso
fraccion1 = Fracción(1, 2)
fraccion2 = Fracción(3, 4)

suma = fraccion1 + fraccion2
print("Suma:", suma)

resta = fraccion1 - fraccion2
print("Resta:", resta)

division = fraccion1 / fraccion2
print("División:", division)
