# completa el código de la función
class Cuenta:
    def __init__(self,rut,saldo):
      self.saldo=saldo
      self.rut=rut
    def girar(self,monto):
      if monto<=self.saldo:
        self.saldo-=monto
        return True
      else:
        return False 
