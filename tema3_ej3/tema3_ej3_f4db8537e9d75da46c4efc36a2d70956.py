# completa el código de la función
class Cuenta:
     def_init(self,rut,saldo):
     self.rut = rut
     self.saldo = saldo
  def girar(self,monto):
     if self.saldo>=monto:
     self.saldo -= monto
     return True
  else:
     return False
  pass
           