class Cuenta:
  def __init__(self,rut,saldo):
    self.rut=rut
    self.saldo=saldo
  def girar(self,giro):
    if giro>self.saldo:
      return False
    if giro<=self.saldo:
      self.saldo-=giro
      return True