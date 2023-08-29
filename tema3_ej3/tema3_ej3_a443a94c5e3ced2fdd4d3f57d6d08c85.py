# completa el código de la función
# completa el código de la función
class Cuenta:
  def __init__(self,r,s):
    self.rut=r
    self.saldo=s
    
  
  def girar(self,giro):
    if self.saldo > giro:
      self.saldo=self.saldo-giro
      return True
    else:
      return False
