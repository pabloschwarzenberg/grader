# completa el código de la función
class Cuenta:
    def __init__(self, rut, saldo):
        self.rut = rut
        self.saldo = saldo

    def girar(self, monto):
        giro = False
        if monto <= self.saldo:
            self.saldo = self.saldo - monto
            giro = True
        return giro

           