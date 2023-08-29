# completa el código de la función
class Cuenta:
  def __init__ (self,rut,saldo):      
      self.rut = rut
      self.saldo = saldo
  def girar(self,giro):
      self.giro = giro
      self.saldo = self.saldo - giro
      if self.saldo >= 0:
          return True          
      else:
          return False

micuenta = Cuenta("18654636-9",100000)
print("El rut es:", micuenta.rut)
print("Mi saldo es:", micuenta.saldo)
print("Puedes realizar el giro?")
print(micuenta.girar(50000))