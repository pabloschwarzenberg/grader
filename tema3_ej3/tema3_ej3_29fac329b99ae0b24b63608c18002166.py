# completa el código de la función
class Cuenta:
    def __init__(self, rut, saldo):
        self.rut = rut
        self.saldo = saldo

    def girar(self, x):
        if self.saldo >= x:
            self.saldo = self.saldo - x
            return True
        else: 
            return False
           