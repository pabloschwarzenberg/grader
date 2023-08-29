# completa el código de la función
class Cuenta:
    def __init__(self,rut,saldo):
        self.rut=rut
        self.saldo=saldo

    def girar(self,monte):
        if monte<=self.saldo:
            self.saldo=self.saldo-monte
            return True
        else:
            return False 