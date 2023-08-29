# completa el código de la función
class Cuenta:
  def __init__(self,rut,saldo):
    self.rut=rut
    self.saldo=saldo
    
  def girar(self,saldo2):
     self.saldo2=saldo2
     if self.saldo>saldo2:
         total=self.saldo-saldo2
         self.saldo=total
         return True
     else:
         return False
           