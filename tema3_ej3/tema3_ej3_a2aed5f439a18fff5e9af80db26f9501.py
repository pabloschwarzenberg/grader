# completa el código de la función
class Cuenta:
    def __init__(self,rut,saldo):
        self.rut = rut
        self.saldo = saldo
    def girar (self,monto):
        giro = False
        if self.saldo >= monto:
            giro = True
        else:
            giro = False
        if giro:
            self.saldo = self.saldo-monto
        return giro  