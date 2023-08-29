# completa el código de la función
class Cuenta:
  def __init__(self,rut,saldo):
    self.rut = rut
    self.saldo = int(saldo)
    
  def girar(self,monto):
    if self.saldo >= int(monto):
      self.saldo = self.saldo - int(monto)
      return True
     
    elif self.saldo < int(monto):
      return False
           