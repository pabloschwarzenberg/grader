# completa el código de la función
class Cuenta:
  def __init__(self,rut,saldo):
      self.rut = rut
      self.saldo = saldo
  def girar(self,monto):
      if monto<=saldo:
           self.saldo = self.saldo-monto
           return True
      else:
           return False

rut = "12345678-9"
saldo = 10000
monto = 11000
