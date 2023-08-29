# completa el código de la función
class Cuenta:
  def __init__(self,rut,saldo):
    self.rut=rut
    self.saldo=saldo
  def girar(self,g):
    if self.saldo>=g:
      self.saldo-=g
      return True
    else:
      return False