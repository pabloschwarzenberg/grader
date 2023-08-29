# completa el código de la función
class Cuenta:
  def __init__(self,rut,saldo):
      self.rut=rut
      self.saldo=saldo
  def __repr__(self):
    return self.saldo
  def girar(self,giro):
    if self.saldo>=giro:
      nuevo_saldo=self.saldo-giro
      self.saldo=nuevo_saldo
      return True
    else:
      return False
           