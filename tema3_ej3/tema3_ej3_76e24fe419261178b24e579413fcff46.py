#Cuenta Corriente en un Banco 2/2 points (ungraded)
class Cuenta:
  def _init_(self, r, s):
    self.rut = r
    self.saldo = s

  def girar(self, giro):
    if self.saldo > giro:
      self.saldo = self.saldo-giro
      return True
    else:
      return False


           