# completa el código de la función
class Cuenta:
    def __init__(self,rut,saldo):
        self.rut=rut
        self.saldo=saldo

    def girar(self, cantidad):
        if self.saldo>=cantidad:
            self.saldo-=cantidad
            return True
        else:
            return False
        
