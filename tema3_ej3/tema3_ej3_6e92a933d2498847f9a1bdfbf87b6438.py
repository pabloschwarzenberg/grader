class Cuenta:
  def __init__(self,rut,saldo):
    self.rut=rut
    self.saldo=saldo
    
  def girar(self,giro):
    if self.saldo>giro:
      self.saldo-=giro
      return True
    else:
      return False
            