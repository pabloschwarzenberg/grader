class Cuenta:
  def __init__(self, rut, saldo):
    self.rut = rut
    self.saldo= saldo
  def girar(self, retirar):
    self.retirar = retirar
    if self.retirar<=self.saldo:
      self.saldo = self.saldo - self.retirar
      return True
    else:
      return False

           