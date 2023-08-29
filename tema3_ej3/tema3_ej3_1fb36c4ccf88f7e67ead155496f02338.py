# completa el código de la función
class Cuenta:
  def __init__(self, rut, saldo):
      self.rut = rut
      self.saldo = saldo
  def girar(self, monto):
      if 0 <= monto <= self.saldo:
          self.saldo -= monto
          return True
      else:
          return False
           