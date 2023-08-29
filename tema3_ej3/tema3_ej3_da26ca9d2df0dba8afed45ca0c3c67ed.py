# completa el código de la función
class Cuenta:
    def __init__(self, rut, saldo):
        self.rut = rut
        self.saldo = saldo

    def girar(self, cantidad_giro):
        if cantidad_giro < self.saldo:
            self.saldo -= cantidad_giro
            return True
        else:
            return False