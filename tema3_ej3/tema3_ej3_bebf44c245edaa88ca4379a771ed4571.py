# completa el código de la función
class Cuenta:

  def __init__(self,rut,saldo):
    self.rut=rut
    self.saldo=saldo
 
  def girar(self,girar):
    
    if girar<=self.saldo and girar>0:
      self.saldo= self.saldo- girar
      return True
    else:
      return False