# completa el código de la clase
class Cuenta:
  def __init__(self,rut,saldo):
    self.rut=rut
    self.saldo=saldo
  def girar(self,monto_a_sacar):
    if self.saldo>=monto_a_sacar:
      self.saldo=self.saldo-monto_a_sacar
      return True
    else:
      return False
  pass
           