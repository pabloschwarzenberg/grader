class Cuenta:

    def __init__(self,rut,saldo):
        self.rut=rut
        self.saldo=saldo

    def girar(self,giro):
        if self.saldo>=giro:
            self.saldo=self.saldo-giro
            return True
        else:
            return False

cuenta=Cuenta("19.819.078-0",28000)
cuenta.girar(15000)
           