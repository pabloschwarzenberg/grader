# completa el código de la función
class Cuenta:
  def __init__(self,rut,saldo):
    self.rut=rut
    self.saldo=saldo
    
  def girar (self,money):
    if money<=self.saldo:
      self.saldo-=money
      return True
    else: return False