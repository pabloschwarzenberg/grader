# completa el código de la función
class Cuenta:
  def __init__(self,rut,saldo):
    self.rut=rut
    self.saldo=saldo
  def girar(self,monto):
    if monto <= int(self.saldo):
        self.saldo=int(self.saldo)-monto
        return True
    else:
        return False
  
           