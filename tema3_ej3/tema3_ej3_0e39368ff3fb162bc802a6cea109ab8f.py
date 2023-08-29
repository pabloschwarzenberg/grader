# completa el código de la clase
class Cuenta:
  def __init__(self,rut,saldo):
    self.rut=rut
    self.saldo=saldo
  def girar(self, saldo_a_retirar):
    if self.saldo>=saldo_a_retirar:
      self.saldo=self.saldo-saldo_a_retirar
      return True
    else:
      return False
           