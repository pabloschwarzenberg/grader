class Cuenta:
  def __init__(self,rut,saldo):
    self.rut=rut
    self.saldo=saldo
    
  def girar(self,saldo1):
    if self.saldo>=saldo1:
      self.saldo=self.saldo-saldo1
      return True
    else:
      return False  