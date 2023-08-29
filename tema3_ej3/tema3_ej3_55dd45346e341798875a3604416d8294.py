# completa el código de la función
class Cuenta:
  def __init__(self, argrut, argsaldo):
    self.rut = argrut           
    self.saldo = argsaldo
  def girar(self,monto):
    if monto <= self.saldo:
      self.saldo -= monto
      return True
    else:
      return False          