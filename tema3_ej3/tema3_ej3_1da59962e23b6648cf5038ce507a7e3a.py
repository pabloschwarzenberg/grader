# completa el código de la función
class Cuenta:
  def __init__(self,rut,saldo):
    self.r=rut
    self.s=saldo
  def girar(self,monto):
    if self.s>monto:
      return True
    else:
      return False
           