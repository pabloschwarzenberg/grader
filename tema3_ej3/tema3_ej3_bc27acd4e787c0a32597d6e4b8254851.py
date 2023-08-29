class Cuenta:
  def __init__(self,rut,saldo):
      self.rut=rut
      self.saldo=float(saldo)
      
  def girar(self,monto):
      monto=int(monto)
      if self.saldo<monto:
          return False
      elif self.saldo>=monto:
          self.saldo=self.saldo - monto
          print("Nuevo saldo: ",self.saldo)
          return True
          
           