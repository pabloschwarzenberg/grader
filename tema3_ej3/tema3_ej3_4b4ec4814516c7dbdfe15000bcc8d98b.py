# completa el código de la clase
class Cuenta:
    def __init__(self,rut,saldo):
        self.rut=rut
        self.saldo=int(saldo)
        
    def girar(self,giro):
        self.giro=int(giro)
        if self.giro < self.saldo:
            self.saldo=self.saldo-self.giro
            return True
        else:
            return False
        
    def __str__(self):
        return str(self.saldo)
           