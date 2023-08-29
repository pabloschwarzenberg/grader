# completa el código de la función
class Cuenta:
    def __init__(self,rut,saldo):
        self.r = rut
        self.s = saldo

    def girar(self, giro):
        self.g = giro
        if self.g <= self.s:
            self.s -= self.g
            print(self.s)
            return True