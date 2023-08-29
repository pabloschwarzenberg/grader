# completa el código de la función
class Cuenta:
  def __init__(self,rut,saldo):
    self.rut=rut
    self.saldo=saldo
  def girar(self,monto):
    b=monto
    a=self.saldo
    if a>b:
      self.saldo-=monto
      return True
    else:
      return False 