class Cuenta:
    def __init__(self,rut,saldo):
        self.rut=rut
        self.saldo=int(saldo)
    def girar(self, plata):
        if int(plata) > self.saldo:
            return False
        else:
            self.saldo=self.saldo-int(plata)
            return True