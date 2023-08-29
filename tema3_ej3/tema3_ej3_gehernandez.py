class Cuenta:
    def __init__(self,rut,saldo):
        self.rut=rut
        self.saldo=saldo
    def girar(self,sacar):
        if sacar>0 and sacar<=self.saldo:
            self.saldo=self.saldo-sacar
            return True
        else:
            return False

           