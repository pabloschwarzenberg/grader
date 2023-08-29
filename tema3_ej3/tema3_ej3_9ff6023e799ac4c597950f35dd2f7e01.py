# completa el código de la función
class Cuenta:
  def __init__(self,rut,saldo):
    self.rut=rut
    self.saldo=saldo
  def girar(self,retirar):
    if self.saldo>=retirar:
      self.saldo=(self.saldo)-(retirar)
      return True
    else:
      return False
           