# completa el código de la función
class Cuenta:
  def __init__(self,rut,saldo):
    self.rut=rut
    self.saldo=saldo
    
  def girar(self,saldo2):
    if saldo2<=self.saldo:
      self.saldo=self.saldo-saldo2
      return True
    else:
      return False
 
           