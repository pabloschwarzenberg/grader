# completa el código de la función
class Cuenta:
  def __init__(self,rut,saldo):
    self.rut=rut
    self.saldo=saldo
  def girar (self,cantidad):
    print(cantidad<=self.saldo)
    if cantidad<=self.saldo:
      self.saldo=self.saldo-cantidad
      return True
    return False
 
           