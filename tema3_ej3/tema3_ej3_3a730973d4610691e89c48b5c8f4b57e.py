# completa el código de la función
class Cuenta:
  def __init__(self,rut,saldo):
    self.rut=rut
    self.saldo=saldo
    
  def girar(self,plata):
    if self.saldo>plata:
      self.saldo=self.saldo-plata
      return True
    if self.saldo<plata:
      return False
           