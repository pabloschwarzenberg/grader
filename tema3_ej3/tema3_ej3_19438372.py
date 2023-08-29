# completa el código de la función
class Cuenta():
  def __init__(self,rut,saldo):
    self.rut=rut
    self.saldo=saldo
  def girar(self,monto):
    if int(monto)>int(self.saldo):
      return False
    elif int(monto)<int(self.saldo):
      self.saldo-=int(monto)
      return True
   
           