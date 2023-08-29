class Cuenta:
    def __init__(self,rut,saldo):
        self.rut = rut
        self.saldo = saldo

    def __ge__(self,other):
        if self.saldo <= other.saldo:
            return True
        else:
            return False
        

    def girar(self,giro):
        if self.saldo >= giro:
            self.saldo = self.saldo - giro
            return True
        else:
            return False
        
           