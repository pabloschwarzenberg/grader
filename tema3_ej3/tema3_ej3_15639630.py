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
        self.s=m
        return True

if __name__=="__main__":
    Cliente=Cuenta(1000,19322522-5)
    o=int(input("Ingrese el valor que quiere girar: $"))
    print(Cliente.girar(o))
