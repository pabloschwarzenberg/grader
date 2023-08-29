# completa el código de la función

class Cuenta():
    def __init__(self, rut, saldo):
        self.rut=rut
        self.saldo=saldo
    def girar(self, dinero):
        self.dinero=dinero
        if self.dinero<=int(self.saldo):
            self.saldo=int(self.saldo)-self.dinero
            return True
        else:
            return False
        
        
