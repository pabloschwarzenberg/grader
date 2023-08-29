# completa el código de la función
class Cuenta:
  def __init__(self,rut,saldo):
    self.rut=rut
    self.saldo=saldo
  def girar(self,giro):
      saldo=self.saldo
      if giro<=saldo:
        self.saldo-=giro
        return True 
      else:
        return False
  
           