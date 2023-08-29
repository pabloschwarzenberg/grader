# completa el código de la función
class Cuenta:
  def __init__(self, rut, saldo):
    self.rut = rut
    self.saldo = saldo
    
  def girar(self, giro):
    if self.saldo >= 0:
      self.saldo -= giro
      return True
    return False
           