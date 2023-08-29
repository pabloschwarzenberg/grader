class Cuenta:
    def __init__(self,rut,saldo):
        self.saldo=saldo
        self.rut=rut

    def girar(self,saldo_girar):
        if saldo_girar<self.saldo:
            return True
        self.saldo=self.saldo-saldo_girar
       
       else:
            return False