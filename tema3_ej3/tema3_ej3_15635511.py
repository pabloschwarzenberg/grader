# completa el código de la función
class Cuenta:
  def __init__(self,saldo,rut):
    self.r=rut
    self.s=saldo

  def girar(self,giro):
    t=int(giro)
    m=self.s-t
    if int(m)<0:
        return False
    if int(m)>=0:
        self.s=str(m)
        return True