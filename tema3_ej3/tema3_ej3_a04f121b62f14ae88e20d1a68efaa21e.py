# completa el código de la función
class Cuenta:
    def __init__(self,rut,saldo):
        self.rut=rut
        self.saldo=saldo
    def girar(self,dinero):
         if dinero<=self.saldo:
             self.saldo=self.saldo-dinero
             return True
         else:
             return False  