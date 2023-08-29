# completa el código de la función
class Cuenta:
    def __init__(self,rut,saldo):
        self.rut = rut 
        self.saldo = saldo
        
    def girar(self,monto):     
        if monto <= self.saldo:
            self.saldo = self.saldo-monto
            return True,self.saldo
        else:
            return False
    def __str__(self):
        return "{0},{1}".format(self.rut,self.saldo)
           