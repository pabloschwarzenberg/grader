# completa el código de la función
class Cuenta:
    def   __init__(self,rut,saldo):
        self.rut=rut
        self.saldo=saldo
        
    def girar(self,p):
        if p>self.saldo:
            return False
        else:
            self.saldo=self.saldo-p
            return True
  
           