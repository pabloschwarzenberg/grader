# completa el código de la clase
class Cuenta:
  def __init__(self, rut, saldo):
    self.rut = rut
    self.saldo = saldo
  
  def girar(self, monto):
    if monto <= self.saldo:
      giro = True
      self.saldo -= monto
    else:
      giro = False
    return giro