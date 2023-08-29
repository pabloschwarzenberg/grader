# completa el código de la función
class Cuenta:
    def __init__(self,rut,saldo):
        self.rut=rut
        self.saldo=saldo

    def girar(self,saldo):
        if saldo<=self.saldo:
            self.saldo=self.saldo-saldo
            return True
        elif saldo>self.saldo:
            return False
           