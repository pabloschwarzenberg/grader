class Cuenta:
    def __init__(self,rut,saldo):
        self.rut=""
        self.saldo=saldo
        
    def girar(self,giro):
        if self.saldo>=giro:
            self.saldo=self.saldo-giro
            return True
        elif self.saldo<giro:
            return False           