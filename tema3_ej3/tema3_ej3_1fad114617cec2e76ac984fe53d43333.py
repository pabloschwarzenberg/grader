# completa el código de la función
class Cuenta:
  def __init__(self,rut,saldo):
    self.rut=rut
    self.saldo=saldo
    self.giro=0
  def girar(self,giro):
    self.giro+=giro
    if self.giro<=self.saldo:
      self.saldo=self.saldo-self.giro
      return True
    else:
      return False
    
  
           