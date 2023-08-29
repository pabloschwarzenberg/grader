class Cuenta:
    def __init__(self,rut,saldo):
        self.saldo=saldo
        self.rut=rut
    def girar(self,saldo):
        if saldo>self.saldo:
            return False
        else:
            self.saldo=self.saldo-saldo
            return True
            

  
           