# completa el código de la función
class Cuenta:
  def __init__(self,rut,saldo):
    self.rut=rut
    self.saldo=saldo

  def girar(self,giro):
    if giro<=self.saldo:
        self.saldo=(self.saldo)-giro
        return True
    else:
        return False

  def __str__(self):
    return "{0},{1}".format(self.rut,self.saldo)

p1=Cuenta("19247066-8",200)

print(p1)



