# completa el código de la función
class Cuenta:
    def __init__(self, rut, saldo):
        self.rut=rut
        self.saldo=saldo

    def girar(self,monto):
        if monto>self.saldo:
            return False
        if monto<=self.saldo:
            self.saldo=self.saldo-monto

    
           