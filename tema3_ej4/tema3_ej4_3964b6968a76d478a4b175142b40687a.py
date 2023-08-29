def __init__(self, numerador, denominador):
    self.numerador = int(numerador)
    if denominador == 0:
        raise Exception("El denominador no puede ser 0")
    self.denominador = int(denominador)

def __str__(self):
    return str(self.numerador) + "/" + str(self.denominador)

def equivalente(self, otra): #otra: Fraccion
    return self.denominador == otra.denominador and self.numerador == otra.numerador

def maximo_comun_divisor(self, a, b):
    temporal = 0
    while b != 0:
        temporal = b
        b = a % b
        a = temporal
    return a
otra = 'Fraccion'
def minimo_comun_multiplo(self, a, b):
    return (a * b) / self.maximo_comun_divisor(a, b)

def suma(self, otra):
    mcm = self.minimo_comun_multiplo(self.denominador, otra.denominador)
    diferencia_self = mcm/self.denominador
    diferencia_otra = mcm/otra.denominador
    numerador_resultado = (diferencia_self*self.numerador) + \
        (diferencia_otra*otra.numerador)
    return otra(numerador_resultado, mcm)

def resta(self, otra):
    mcm = self.minimo_comun_multiplo(self.denominador, otra.denominador)
    diferencia_self = mcm/self.denominador
    diferencia_otra = mcm/otra.denominador
    numerador_resultado = (diferencia_self*self.numerador) - \
        (diferencia_otra*otra.numerador)
    return otra(numerador_resultado, mcm)

def producto(self, otra):
    return otra(self.numerador*otra.numerador, self.denominador*otra.denominador)

def cociente(self, otra):
    return otra(self.numerador*otra.denominador, self.denominador*otra.numerador)

def inversa(self):
    return otra(self.denominador, self.numerador)

def potencia(self, exponente):
    return otra(self.numerador ** exponente, self.denominador ** exponente)

def simplifica(self):
    mcd = self.maximo_comun_divisor(self.numerador, self.denominador)
    return otra(self.numerador / mcd, self.denominador / mcd)

def a_mixta(self):
    return otra.a_mixta(self)
