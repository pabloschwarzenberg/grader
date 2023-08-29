class Cuenta:
    def __init__(self,rut,saldo):
        self.rut=rut
        self.saldo=saldo
    def girar(self,monto):
        self.monto=monto
        girar=True
        if monto>self.saldo:
            girar=False
        else:
            self.saldo=self.saldo-monto
        return girar

