# completa el código de la función
class Cuenta:
  def __init__(self, rut, saldo):
    self.rut = rut
    self.saldo = saldo
    
  def girar(self, monto):
    if monto <= self.saldo:
      self.saldo -= monto
      return True
    return False
           
if __name__ == "__main__":
    cuenta=Cuenta(204834603, 50000)
    cuenta.girar(5000)