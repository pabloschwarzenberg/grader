def __init__(self, numerador, denominador):
    self.numerador = int(numerador)
    if denominador == 0:
        raise Exception("El denominador no puede ser 0")
    self.denominador = int(denominador)

def __str__(self):
    return str(self.numerador) + "/" + str(self.denominador)

def equivalente(self, otra: 'Fraccion') -> bool:
    return self.denominador == otra.denominador and self.numerador == otra.numerador