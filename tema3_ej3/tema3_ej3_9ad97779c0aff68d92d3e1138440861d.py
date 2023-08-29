# completa el código de la función
class Cuenta:
  def __init__(self,rut,saldo):
    self.rut=rut
    self.saldo=saldo
  
  def girar(self,monto):
    self.saldofinal=self.saldo-monto
    if self.saldofinal>=0:
      self.saldo=self.saldofinal
      return True
    else:
      return False
  
           