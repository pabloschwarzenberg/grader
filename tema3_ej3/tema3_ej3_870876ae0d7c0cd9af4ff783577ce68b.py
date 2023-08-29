class Cuenta:
  def __init__(self,rut,saldo):
    self.rut = rut
    self.saldo = saldo
  def girar(self,cantidad):
    if self.saldo >=cantidad:
      self.saldo = self.saldo - cantidad
      return True,self.saldo
    else:
      return False