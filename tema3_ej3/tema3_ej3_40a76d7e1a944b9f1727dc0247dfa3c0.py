# completa el código de la función
class Cuenta:
  def __init__(self,rut,saldo): # constructor necesita llenar los atrivutos
    self.rut=rut 
    self.saldo=saldo
  
  def girar(self,monto):
    if monto<self.saldo:
      self.saldo=self.saldo-monto
      return True
    else:
      return False

obj_cuenta=Cuenta("21585095-1",10000)
obj_cuenta.girar(7000)
print(obj_cuenta.saldo)
           