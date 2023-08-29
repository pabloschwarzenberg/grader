# completa el código de la función
class Cuenta:
  def __init__(self, rut, saldo):    
    self.saldo=saldo
    self.rut=rut
    
  def girar(self, xxx):
    if xxx<=self.saldo:
      self.saldo-=xxx
      return True
    else:
      return False