# completa el código de la clase
class Cuenta:
  def __init__(self,rut,saldo):
    self.rut=rut
    self.saldo=saldo
   
  def girar(self,agirar):
    if int(self.saldo)>=int(agirar):
      self.saldo=int(self.saldo)-int(agirar)
      return True
    else:
      return False