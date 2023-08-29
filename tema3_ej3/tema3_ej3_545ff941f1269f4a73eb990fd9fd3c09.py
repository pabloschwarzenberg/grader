# completa el código de la función
class Cuenta:
  def __init__(self,rut,saldo):
    self.rut=rut
    self.saldo=saldo
  def girar(self,monto):
    if int(self.saldo)>int(monto):
      self.saldo=int(self.saldo)-int(monto)
      return True
    if int(self.saldo)<int(monto):
      return False
           