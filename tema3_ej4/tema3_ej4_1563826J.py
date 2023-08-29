class Fraccion:
    def __init__(self,numerador,denominador):
        self.numerador=numerador
        self.denominador=denominador
    def __mul__ (self,f2):
        numerador_f3=self.numerador*f2.numerador
        denominador_f3=self.denominador*f2.denominador
        return str(numerador_f3)+'/'+str(denominador_f3)
    def __add__(self,f2):
        denominador_f3=self.denominador*f2.denominador
        numerador_f3=self.numerador*f2.denominador+self.denominador*f2.numerador
        return str(numerador_f3)+'/'+str(denominador_f3)
    def __sub__(self,f2):
        denominador_f3=self.denominador*f2.denominador
        numerador_f3=self.numerador*f2.denominador-self.denominador*f2.numerador
        return str(numerador_f3)+'/'+str(denominador_f3)
    def __truediv__ (self,f2):
        numerador_f3=self.numerador*f2.denominador
        denominador_f3=self.denominador*f2.numerador
        return str(numerador_f3)+'/'+str(denominador_f3)
        
    def __str__(self):
        '{0}/{1}'.format(self.numerador,self.denominador)