# completa el código de la clase
class Cuenta:
    def __init__(self,rut,saldo):
        self.rut=rut
        self.saldo=saldo


    def girar(self,retirar):
        if retirar <= self.saldo:
            self.saldo=self.saldo-retirar
            return True
        else:
            return False
