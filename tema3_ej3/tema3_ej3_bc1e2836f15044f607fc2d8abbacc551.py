# completa el código de la clase
class Cuenta:
    def __init__(self,rut,saldo):
        self.rut=rut
        self.saldo=saldo
    def girar(self,monto):
        if monto<=self.saldo:
            self.saldo=self.saldo-monto
            return True
        else:
            return False
           