# completa el código de la función
class Cuenta:
    def __init__(self,rut,saldo):
        self.rut=rut
        self.saldo=saldo
    def girar (self,monto):
        if self.saldo>=monto:
            self.saldo=self.saldo-monto
        return self.saldo>=monto
           