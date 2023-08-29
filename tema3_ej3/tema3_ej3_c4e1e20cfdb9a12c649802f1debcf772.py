# completa el código de la función
class Cuenta:
  def __init__(self,rut,saldo):
    self.rut=rut
    self.saldo=saldo
    
  def girar(self,giro):
    if giro<=self.saldo:
      self.saldo=self.saldo-giro
      return True,self.saldo
    else:
      return False

if __name__== "__main__":
  giro=int(input())
            
           