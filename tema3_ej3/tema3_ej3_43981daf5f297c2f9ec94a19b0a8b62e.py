# completa el código de la función
class Cuenta:
  def __init__(self, rut, saldo):
        self.rut = rut
        self.saldo = saldo

  def girar(self, pagar):
        self.saldo -=  pagar
        if self.saldo >= 0:
            return self.saldo
        else:
            return False
           