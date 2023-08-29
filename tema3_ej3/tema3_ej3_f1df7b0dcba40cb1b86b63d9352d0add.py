# completa el código de la función
class Cuenta:
    def __init__(self,rut,saldo):
        self.rut=rut
        self.saldo=saldo

    def girar(monto,self):
        if monto > self.saldo:
            return False
        else:
            self.saldo=self.saldo-monto
            return True     