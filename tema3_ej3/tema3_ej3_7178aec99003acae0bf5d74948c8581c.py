# completa el código de la función
class Cuenta:
  def __init__(self, rut, saldo):
    self.rut=rut
    self.saldo=saldo
  def girar(self, retiro):
    if (self.saldo-retiro)<0:
      return(False)
    else:
      self.saldo=self.saldo-retiro
      return(True)
  pass
           