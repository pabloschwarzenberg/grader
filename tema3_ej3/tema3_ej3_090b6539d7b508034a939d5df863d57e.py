# completa el código de la función
class Cuenta:
    def __init__(self,rut,saldo):
        self.rut = rut
        self.saldo = saldo
    def girar(self,monto):
        if self.saldo > monto:
            a = self.saldo - monto
            self.saldo = a
            return(True)
        else:
            return(False)
           