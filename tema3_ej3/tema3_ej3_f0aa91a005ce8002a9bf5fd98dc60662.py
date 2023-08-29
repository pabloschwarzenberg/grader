# completa el código de la clase
class Cuenta:
  def __init__(self,rut,saldo):
   self.rut=rut
   self.saldo=saldo
  def girar(self,giro):
   money = self.saldo
   if money >= giro:
    self.saldo -= giro
    return True
   else:
    return False
   

if __name__ == "__main__":
 pass