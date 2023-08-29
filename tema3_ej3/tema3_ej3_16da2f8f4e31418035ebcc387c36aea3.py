# completa el código de la función
class Cuenta:
    def __init__(self,rut,saldo):
        self.rut=rut
        self.saldo=saldo

    def girar(self,giro):
        self.giro=giro
        if self.giro<self.saldo:
            self.resta(self.saldo)
            return True
        else:
            return False

    def resta(self,saldo):
        self.saldo-=self.giro
        return self.giro
           