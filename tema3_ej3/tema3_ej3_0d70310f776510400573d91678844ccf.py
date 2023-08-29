# completa el código de la función
class Cuenta:
  def __init__(self,rut,saldo):
      self.rut=rut
      self.saldo=saldo
      
  def girar(self,saldo_a_girar):
      if self.saldo>=saldo_a_girar:
         self.saldo=self.saldo-saldo_a_girar
         return True
          
      else:
        return False
      
      
  
           