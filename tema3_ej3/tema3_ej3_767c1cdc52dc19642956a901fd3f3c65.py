# completa el código de la clase
class Cuenta:
    def __init__(self,rut,saldo):
        self.rut=rut
        self.saldo=saldo
    def girar(self,monto):
        giro=self.saldo-monto
        if giro>=0:
            self.saldo=self.saldo-monto
            return True
        else:
            return False           