# completa el código de la función
class Cuenta:
  def __init__(self,rut,saldo):
    self.rut=rut
    self.saldo=saldo
  
  def girar(self,monto):
      self.monto=monto
      if self.monto<self.saldo:
        self.saldo=self.saldo-self.monto
        return True
      elif self.saldo<self.monto:      
        return False           