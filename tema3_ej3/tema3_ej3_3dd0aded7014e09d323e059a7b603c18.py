# completa el código de la función
class Cuenta:
  def __init__(self,rut,saldo):
    self.rut=rut
    self.saldo=int(saldo)
    
  def girar(self,giro):
    giro_nuevo=int(giro)
    if (giro_nuevo < self.saldo) or (giro_nuevo == self.saldo):
      self.saldo=self.saldo-giro_nuevo
      return True
    else:
      return False
      
           