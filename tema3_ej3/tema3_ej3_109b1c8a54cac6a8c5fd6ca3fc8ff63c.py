# completa el código de la clase
class Cuenta:
  def __init__(self,rut,saldo):
    self.rut=rut
    self.saldo=int(saldo)
  def girar(self,giro):
    if self.saldo<int(giro):
      return False
    else:
      self.saldo=self.saldo-int(giro)
      return True
  pass
           