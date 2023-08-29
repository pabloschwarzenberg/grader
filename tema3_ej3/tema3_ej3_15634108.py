class Cuenta:
    def __init__(self,rut,saldo):
        self.rut=rut
        self.saldo=saldo
    def girar(self,monto):
        if monto > self.saldo:
            return False
        elif monto<=self.saldo:
            self.saldo=self.saldo-monto
            return True
    def __repr__(self):
        return "RUT usuario: "+str(self.rut)+"\nSaldo: "+str(self.saldo)