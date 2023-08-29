# completa el código de la función
class Cuenta:
  def __init__(self,r,s):
    self.rut=r
    self.saldo=s
    
  def girar(self,giro):
    if self.saldo>giro:
      self.saldo= self.saldo-giro
      return True
    else:
      return False
  
  def __str__(self):
    return "Rut"+str(self.rut)+"###" + "saldo" + str(self.saldo)

a = Cuenta("1-9",10000)
print(a)
r = a.girar(3000)
print(r)
print(a)