__author__ = 'Damian'
class Cuenta:
    def __init__(self, rut, saldo):
        self.rut=rut
        self.saldo=saldo
    def __repr__(self):
        return str(self.rut)+" "+str(self.saldo)
    def __sub__(self, giro):
        if isinstance(giro, int) or isinstance(giro, float):
            saldo=saldo-giro
            return saldo
    def girar(self, x):
        if x>self.saldo:
            return False
        elif x<self.saldo:
            self.saldo = self.saldo - x
            saldo = self.saldo
            print(" Giro realizado, tu nuevo saldo es: ", saldo)
            return True, self.saldo