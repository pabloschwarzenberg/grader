class Cuenta:
  def __init__(self,rut,saldo):
    self.rut=rut
    self.saldo=saldo
  def girar(self,giro):
    self.giro=giro
    self.saldo=(self.saldo-giro)
    if self.saldo>=0:
      return True
    if self.saldo<0:
      return False