class Cuenta:
    def __init__(self,rut,saldo):
        self.rut = rut
        self.saldo = saldo
    def girar(self,giro):
        if int(giro) <= int(self.saldo):
            self.saldo -= int(giro)
            return True
        else:
            return False
        pass