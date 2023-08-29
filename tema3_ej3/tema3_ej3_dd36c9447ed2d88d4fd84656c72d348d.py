class Cuenta:
    def __init__(self,rut,saldo):
        self.rut=rut
        self.saldo=saldo

    def girar(self,girar):        
        if self.saldo>=girar:
            self.saldo-=girar
            return True
        else:
            return False
       
pass
           