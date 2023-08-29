# completa el código de la clase
class Cuenta:
  def __init__(self,rut,saldo):
    self.rut=rut
    self.saldo=saldo
    
  def girar(self,giro):
    saldo=int(self.saldo)
    if giro > saldo:
        return False
    else:
        saldofinal= saldo - giro
        self.saldo= saldofinal
        print (saldofinal)
        return True


           