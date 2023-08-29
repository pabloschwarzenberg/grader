class Cuenta:
    def __init__(self,rut,saldo):
        self.rut = rut
        self.saldo = saldo

    def girar(self,girar):
        if girar<=self.saldo:
            self.saldo = self.saldo - girar
            return True 
        if girar>self.saldo:
            return False
    
      