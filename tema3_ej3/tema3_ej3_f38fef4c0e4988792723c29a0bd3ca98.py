# completa el código de la función
class Cuenta:
  def __init__(self,rut,saldo):
     self.rut=rut
     self.saldo=saldo
  
  def girar(dinero):
     saldo=saldo-dinero
     if saldo<0:
       return False
     else:
       return True
           
 persona=Cuenta(