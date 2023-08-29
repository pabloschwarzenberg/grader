# completa el código de la función
class Cuenta:
  def __init__(self,rut,saldo):
     self.rut=rut
     self.saldo=saldo
  def setRut(self,rut):
     self.rut=rut
  def girar(self,giro):
    if self.saldo-giro<0:
      return False
    else:
      self.saldo=self.saldo-giro
      return True                  