class Cuenta:
    def __init__(self,rut,saldo):
        self.rut= rut
        self.saldo= saldo
    def girar(self,giro):
        if self.saldo<giro:
            return False
        else:
            self.saldo-=giro
            return True