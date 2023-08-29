class Cuenta:
  def __init__(self,rut,saldo):
      self.rut = rut
      self.saldo = saldo
      
  def girar(self,gir):
      sigira = False
      if gir < self.saldo:
        sigira = True
        self.saldo = self.saldo - gir
      return sigira