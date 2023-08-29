# completa el código de la función
class Cuenta:
  def __init__(self,rut,saldo):
    self.rut = rut
    self.saldo = saldo
  def girar (self,cuanto):
    if int(cuanto) <= self.saldo:
      self.saldo = int(self.saldo) - int(cuanto)
      return True
    if int(cuanto) >= self.saldo:
      return False
           
           