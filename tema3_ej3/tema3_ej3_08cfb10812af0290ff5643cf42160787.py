class Cuenta:
    def __init__(self, rut, saldo):
        self.rut = rut
        self.saldo = saldo

    def girar(self, giro):
        self.giro=giro
        if self.saldo>=self.giro:
            self.saldo=self.saldo-self.giro
            return True
        else:
            return False

