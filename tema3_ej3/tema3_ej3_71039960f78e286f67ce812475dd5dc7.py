class Cuenta:
  def __init__(self,rut,saldo):
      self.rut = rut
      self.saldo = saldo
      
  def girar(self,gir):
      sepuede = False
      if gir < self.saldo:
        sepuede = True
        self.saldo = self.saldo - gir
      return sepuede
      