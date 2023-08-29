# completa el código de la función
class Cuenta:
  def __init__(self,rut,saldo):
    self.rut=rut
    self.saldo=saldo
  
  def girar(self,giro):
    self.saldo=int(self.saldo)
    if self.saldo<giro:
       return False
    else:
       self.saldo=int(self.saldo)-int(giro)
       return True
    
    
           