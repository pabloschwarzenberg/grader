class Cuenta:
    def __init__(self,rut,saldo):
        if isinstance(saldo,int)==True:
            self.rut=rut
            self.saldo=saldo
    
    def girar(self,giro):
        if giro>self.saldo:
            return False
        self.saldo=self.saldo-giro
        return True