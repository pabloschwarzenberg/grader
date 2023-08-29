class Cuenta:
  def __init__(self, rut, saldo):
    self.rut = rut
    self.saldo = saldo
    
  def girar(self, otro):
    giro = self.saldo - otro
    if giro >= 0:
      self.saldo = self.saldo - otro
      return(True)
    else:
      return(False)
           