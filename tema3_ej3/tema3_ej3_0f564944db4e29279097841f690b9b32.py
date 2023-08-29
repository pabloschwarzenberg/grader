class Cuenta:
    def __init__(self,rut,saldo):
      self.rut=rut
      self.saldo=saldo
    def girar(self,saldo):
        if self.saldo>=saldo:
            self.saldo=self.saldo-saldo
            return True
        else:
            return False

           