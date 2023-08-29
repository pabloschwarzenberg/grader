# completa el código de la función
class Cuenta:
  def __init__(self,rut,saldo):
    self.rut=rut
    self.saldo=saldo
  def girar(self,a):
    if self.saldo>=a:
      self.saldo-=a
      return True
    else:
      return False
  pass
           