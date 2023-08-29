# completa el código de la función
class Cuenta:
  def __init__(self,rut,saldo):
    self.rut = rut
    self.saldo = saldo
  def girar(self,sacar):
    if self.saldo >= sacar:
      a = True
      self.saldo = self.saldo - sacar
    else:
      a = False
    return a
           