# completa el código de la función
class Cuenta:
  def __init__ (self,rut,saldo):
    self.rut=rut
    self.saldo=saldo
  def girar(self,monto_giro):
    if self.saldo<monto_giro:
      return False
    if self.saldo>monto_giro:
      self.saldo=self.saldo-monto_giro
      return self.saldo