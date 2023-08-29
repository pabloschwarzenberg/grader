# completa el código de la función
class Cuenta:
    def __init__(self,rut,saldo):
        self.saldo=saldo
        self.rut=rut
    def girar(self,monto):
        self.monto=monto
        if self.monto > self.saldo:
            return 2==3
        elif self.monto < self.saldo:
            self.saldo=self.saldo-self.monto
            return 2==2
           