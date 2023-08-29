# completa el código de la función
class Cuenta:
    def __init__(self, rut, saldo):
        self.rut = rut
        self.saldo = saldo

    def girar(self, pagar):
        calcular = self.saldo - pagar
        if calcular >= 0:
            self.saldo = calcular
            return self.saldo
        else:
            return False
           