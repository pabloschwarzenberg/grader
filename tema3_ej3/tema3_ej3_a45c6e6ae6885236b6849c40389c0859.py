class Cuenta:
  def __init__(self, rut, saldo):
    self.rut = rut
    self.saldo = saldo
  def girar(self, giro):
    if giro > 0 and giro < self.saldo: 
        self.saldo = self.saldo - giro
        return True
    else:
      return False

           