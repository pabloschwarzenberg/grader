# completa el código de la función
class Cuenta:
    
    def __init__(self, rut, saldo):
        self.rut=rut
        self.saldo=saldo

    def girar(self,other):
        if self.saldo>other:
            self.saldo=self.saldo-other
            return True
        else:
            return False
  
           