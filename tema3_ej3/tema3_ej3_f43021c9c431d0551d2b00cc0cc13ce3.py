class Cuenta:
    def __init__(self,rut,saldo):
        self.rut=rut
        self.saldo=saldo

    def girar(self,monto):
        if self.saldo>=monto:
            self.saldo=self.saldo-monto
            return True
        elif self.saldo<monto:
            return False 
           