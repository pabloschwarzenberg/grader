# completa el código de la función
class Cuenta:
    def __init__(self,rut="",saldo=10000):
        self.rut=""
        self.saldo=10000
    def setsaldo(self,saldo):
        self.saldo=saldo
    def girar(self,n):
        if n>self.saldo:
            self.saldo=self.saldo
            return False
        else:
            self.saldo-=n
            return self.saldo
    def __str__(self):
        return "rut del titular: "+self.rut+", saldo: "+ str(self.saldo)
usuario=Cuenta()
if __name__=="__main__":
  usuario.setrut(10000)
  usuario.setsaldo(int(input("Ingrese su saldo: ")))
  print(usuario)
  giro=int(input("Ingrese el monto a girar: "))
  u=usuario.girar(giro)
  if u:
      usuario.setsaldo(usuario.saldo-giro)
      print("Giro exitoso. Su nuevo saldo es",usuario.saldo)
  else:
      print("Saldo insuficiente. Su saldo es",usuario.saldo)