# completa el código de la función
class Cuenta:
    def __init__(self,rut,saldo):
        self.rut=rut
        self.saldo=saldo
    def girar(self, n):
        if n>self.saldo:
            return False
        elif n<=self.saldo:
            self.saldo=self.saldo-n
            print('Su saldo es',self.saldo)
            return True
           