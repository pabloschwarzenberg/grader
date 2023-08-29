# completa el código de la función
class Cuenta:
    def__init__(self,rut,saldo):
        self.rut= rut
        self.saldo= saldo 
        
    def girar_monto (self,monto):
        if self.saldo>=monto:
            self.saldo-=monto
            return True
        else:
            return False
           