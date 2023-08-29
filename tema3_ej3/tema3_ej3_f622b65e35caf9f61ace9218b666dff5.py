# completa el código de la función
class Cuenta:
  def __init__(self,rut,saldo):
    self.rut=rut
    self.saldo=saldo
  def girar(self,giro):
    self.giro=giro
    if int(self.giro)>int(self.saldo):
      return(False)
    else:
      self.saldo=int(self.saldo)-int(self.giro)
      return(True)   