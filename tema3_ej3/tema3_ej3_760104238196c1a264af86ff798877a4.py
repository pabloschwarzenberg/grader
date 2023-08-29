# completa el código de la función
class Cuenta:
    def __init__(self, rut, saldo):
        self.rut = rut
        self.saldo = saldo

    def girar(self, plata):
        if plata <= self.saldo:
            self.saldo -= plata
        return plata <= self.saldo
