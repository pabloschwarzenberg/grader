class Cuenta:

    def __init__(self,rut,saldo):
        self.rut=str(rut)
        self.saldo=int(saldo)

    def girar(self,giro):
        self.giro=int(giro)
        monto=self.saldo-self.giro
        if monto<0:
            return False
        else:
            self.saldo=monto
            return True
                
        