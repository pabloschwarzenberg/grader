# completa el código de la función
class Cuenta:
    def __init__(self,rut,saldo):
        self.rut=rut
        self.saldo=saldo
    def girar(self,cantidad):
        if cantidad>self.saldo:
            return False
        else:
            self.saldo=self.saldo-cantidad
            return True
    def __str__(self):
        return "{0},{1}".format(self.rut,self.saldo)
if __name__=="__main__":
  rut=int(input("Ingresa tu rut: "))
  saldo=int(input("Ingresa tu saldo: "))
  cuenta=Cuenta(rut,saldo)
  print(cuenta)
  giro=int(input("Ingresa el monto que quiere: "))
  print(cuenta.girar(giro))
  print(cuenta)
