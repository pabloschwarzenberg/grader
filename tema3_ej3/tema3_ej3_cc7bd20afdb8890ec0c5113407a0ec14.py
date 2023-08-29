# completa el código de la función
class Cuenta:
    def __init__(self,rut,saldo):
      self.saldo = saldo
      self.rut = rut
    def girar(self,monto):
        if self.saldo>monto:
            saldo2 = self.saldo-monto
            self.saldo = saldo2
            return(True,saldo2)
        else:
            return False