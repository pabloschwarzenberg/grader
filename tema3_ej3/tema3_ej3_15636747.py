# completa el código de la función
class Cuenta:
    def __init__(self,rut,saldo):
      self.rut=rut
      self.saldo=saldo

    def girar(self,giro):
        self.giro=giro
        if self.giro>self.saldo:
            return False
        else:
            self.saldo=self.saldo-self.giro
            return True

           