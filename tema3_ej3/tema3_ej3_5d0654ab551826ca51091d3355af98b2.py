# completa el código de la clase
class Cuenta:
  def __init__(self,rut,saldo):
    self.rut=rut
    self.saldo=saldo
  def girar(self,monto):
    saldo_final=self.saldo-monto
    if saldo_final>0:
      self.saldo=saldo_final
      return True
    if saldo_final<0:
      saldo_final=self.saldo
      return False
           