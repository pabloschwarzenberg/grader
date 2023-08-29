class Cuenta:
    def __init__(self,rut,saldo):
        self.rut=rut
        self.saldo=saldo
    def girar(self,retiro):
        if retiro<self.saldo:
            self.saldo=self.saldo-retiro
            return True
        elif retiro>self.saldo:
            return False
           